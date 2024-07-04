<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Upload de Arquivos XML</title>
  <link rel="stylesheet" href="style.css" />
</head>
<body>
  <div class="container">
    <?php
    // Verifica se o formulário foi submetido
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        // Verifica se arquivos foram enviados
        if(isset($_FILES['xmlFiles'])) {
            // Caminho para onde os arquivos serão enviados (pasta uploads)
            $uploadDir = 'uploads/';

            // Contador para controlar múltiplos arquivos
            $numFiles = count($_FILES['xmlFiles']['name']);

            // Itera sobre cada arquivo enviado
            for ($i = 0; $i < $numFiles; $i++) {
                // Obtém o nome original do arquivo
                $fileName = $_FILES['xmlFiles']['name'][$i];

                // Caminho completo para salvar o arquivo
                $uploadFile = $uploadDir . basename($fileName);

                // Verifica se o arquivo é do tipo XML
                $fileType = strtolower(pathinfo($uploadFile, PATHINFO_EXTENSION));
                if($fileType != "xml") {
                    echo "Apenas arquivos XML são permitidos para o arquivo '$fileName'.<br>";
                } else {
                    // Move o arquivo do diretório temporário para o destino final
                    if (move_uploaded_file($_FILES['xmlFiles']['tmp_name'][$i], $uploadFile)) {
                        echo "Arquivo '$fileName' foi enviado com sucesso para '$uploadDir'.<br>";
                    } else {
                        echo "Erro ao enviar o arquivo '$fileName'.<br>";
                    }
                }
            }
        } else {
            echo "Nenhum arquivo enviado.";
        }
    }
    ?>
    <form method="post" enctype="multipart/form-data">
      <label for="xmlFiles">
        <span>Selecione seus arquivos XML:</span>
      </label>
      <input type="file" name="xmlFiles[]" id="xmlFiles" multiple/>
      <br />
      <div>
        <input type="submit" value="Enviar" id="submit" />
      </div>
    </form>
  </div>
</body>
</html>
