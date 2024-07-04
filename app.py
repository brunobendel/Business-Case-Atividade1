from asyncio import sleep
import xml.etree.ElementTree as ET
import os
import pandas as pd
import locale
import xmltodict

# Diretório onde os arquivos XML são enviados pelo PHP
caminho_uploads = r"C:\Users\bruno\OneDrive\Área de Trabalho\case_DHL\uploads"

# Solicitar ao usuário o nome do arquivo XML que deseja processar (incluindo a extensão)
nome_arquivo = input("Digite o nome do arquivo XML que deseja processar (incluindo a extensão): ")

# Caminho completo para o arquivo XML
caminho_arquivo = os.path.join(caminho_uploads, nome_arquivo)

with open(caminho_arquivo, "rb") as arquivo_nfs:
    dic_nf = xmltodict.parse(arquivo_nfs)

# Convertendo o dicionário de volta para XML string
xml_str = xmltodict.unparse(dic_nf, pretty=True)

# Parse do XML
root = ET.fromstring(xml_str)

# Função auxiliar para remover namespace
def remove_namespace(tree):
    for elem in tree.iter():
        elem.tag = elem.tag.split('}', 1)[-1]
        elem.attrib = {k.split('}', 1)[-1]: v for k, v in elem.attrib.items()}

remove_namespace(root)

# Extração do número da nota fiscal
numero_nf = root.find(".//ide//nNF").text if root.find(".//ide//nNF") is not None else "sem_numero"

# Lista para armazenar os dados
data = []

# Extração dos dados de <det>
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

for det in root.findall(".//det"):
    # Conversão da quantidade para float
    quantidade = float(det.find(".//prod//qCom").text) if det.find(".//prod//qCom") is not None else None
    
    # Conversão do valor unitário para float e formatação monetária
    valor_unitario = float(det.find(".//prod//vUnCom").text) if det.find(".//prod//vUnCom") is not None else None
    valor_unitario_formatado = locale.currency(valor_unitario, grouping=True) if valor_unitario is not None else None
    
    # Conversão do valor total para float e formatação monetária
    valor_total = float(det.find(".//prod//vProd").text) if det.find(".//prod//vProd") is not None else None
    valor_total_formatado = locale.currency(valor_total, grouping=True) if valor_total is not None else None
    
    # Extração do pesoB dentro de <vol> que está dentro de <transp>
    peso_total_kg = None
    transp = root.find(".//transp")
    if transp is not None:
        vol = transp.find(".//vol")
        if vol is not None:
            peso_total = float(vol.find(".//pesoB").text) if vol.find(".//pesoB") is not None else None
            if peso_total is not None:
                # Supondo que o pesoB esteja em gramas, converter para quilogramas
                peso_total_kg = peso_total / 1000.0
    
    # Construção do dicionário com os dados formatados
    item = {
        "Produto": det.find(".//prod//xProd").text,
        "Código Produto": det.find(".//prod//cProd").text,
        "Valor Unitário": valor_unitario_formatado,
        "Valor Total": valor_total_formatado,
        "Quantidade": quantidade,
        "Logradouro": None,  # Inicialmente definido como None para <dest>
        "Número": None,
        "Bairro": None,
        "Código Município": None,
        "Município": None,
        "Estado": None,
        "CEP": None,
        "Código País": None,
        "País": None,
        "Telefone": None,
        "Peso Total (Kg)": peso_total_kg,
    }
    
    # Adicionar o item à lista de dados
    data.append(item)

# Extração dos dados de <dest> (destinatário)
dest = root.find(".//dest")

if dest is not None:
    # Extração das informações do destinatário
    endereco_dest = dest.find(".//enderDest")
    if endereco_dest is not None:
        for item in data:
            item["Logradouro"] = endereco_dest.find(".//xLgr").text if endereco_dest.find(".//xLgr") is not None else None
            item["Número"] = endereco_dest.find(".//nro").text if endereco_dest.find(".//nro") is not None else None
            item["Bairro"] = endereco_dest.find(".//xBairro").text if endereco_dest.find(".//xBairro") is not None else None
            item["Código Município"] = endereco_dest.find(".//cMun").text if endereco_dest.find(".//cMun") is not None else None
            item["Município"] = endereco_dest.find(".//xMun").text if endereco_dest.find(".//xMun") is not None else None
            item["Estado"] = endereco_dest.find(".//UF").text if endereco_dest.find(".//UF") is not None else None
            item["CEP"] = endereco_dest.find(".//CEP").text if endereco_dest.find(".//CEP") is not None else None
            item["Código País"] = endereco_dest.find(".//cPais").text if endereco_dest.find(".//cPais") is not None else None
            item["País"] = endereco_dest.find(".//xPais").text if endereco_dest.find(".//xPais") is not None else None
            item["Telefone"] = endereco_dest.find(".//fone").text if endereco_dest.find(".//fone") is not None else None

# Criação do DataFrame
df = pd.DataFrame(data)

print(df)

# Solicitar que o usuário pressione Enter para sair
input("\nPressione Enter para sair da aplicação...")

# Caminho para salvar o arquivo Excel, usando o número da nota fiscal
caminho_salvar_excel = rf"C:\Users\bruno\OneDrive\Área de Trabalho\case_DHL\dados\excel\nf_{numero_nf}.xlsx"

# Exportação para Excel
df.to_excel(caminho_salvar_excel, index=False)
