# RPA para Processamento de Arquivos XML em Python

Este projeto RPA foi desenvolvido em Python para processar arquivos XML, transformá-los em dados estruturados e exportá-los para Excel. Ele é configurado para operar localmente com arquivos XML ou enviar XML para um servidor PHP para processamento remoto.

## Funcionalidades

- **Processamento Local de XML**: Permite processar arquivos XML localmente a partir de uma pasta específica.
- **Envio de XML para PHP**: Oferece a opção de enviar XML para um site PHP para processamento remoto.
- **Transformação de Dados**: Converte dados XML em um DataFrame pandas para manipulação e análise.
- **Exportação para Excel**: Exporta os dados processados para arquivos Excel, facilitando análises adicionais no Power BI.

## Pré-requisitos

- Python 3.x instalado.
- Bibliotecas Python necessárias instaladas (veja `requirements.txt`).
- Excel instalado para visualização dos dados exportados.

## Instalação e Configuração

1. **Clonar o Repositório:**

   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio
   ```

2. **Instalar Dependências Python:**

   ```bash
   pip install -r requirements.txt
   ```

   Certifique-se de que todas as bibliotecas necessárias, como `pandas` e `xmltodict`, estão instaladas.

3. **Configuração do Ambiente:**

   - Coloque os arquivos XML que deseja processar na pasta `uploads` localizada e edite o caminho `C:\Users\bruno\OneDrive\Área de Trabalho\case_DHL\uploads`.
   - Configure o site PHP para receber XML conforme necessário.
   
   - Para iniciar um servidor local php use:
     ```bash
     php -S localhost:8000
     ```



4. **Execução do Script Python:**

   Execute o script Python para processar os arquivos XML:

   ```bash
   python process_xml.py
   ```

   Siga as instruções no terminal para processar os arquivos XML.

5. **Visualização no Excel e Power BI:**

   Abra os arquivos Excel gerados para visualizar os dados processados. Importe os dados para o Power BI para análises detalhadas e visualizações interativas.

## Uso

- Execute o script Python para processar arquivos XML localmente ou enviar XML para o servidor PHP.
- Utilize os arquivos Excel gerados para análises adicionais no Excel e no Power BI.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](./LICENSE) para mais detalhes.
