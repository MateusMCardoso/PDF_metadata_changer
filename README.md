# 📝 Editor de Metadados de PDF

![Python 3.x](https://img.shields.io/badge/Python-3.x-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

Uma ferramenta de linha de comando simples, rápida e interativa para visualizar e editar os metadados de seus arquivos PDF. Preserve a integridade do seu arquivo original enquanto cria uma nova versão com as informações atualizadas.

## ✨ Principais Funcionalidades

-   **Visualização Clara**: Exibe os metadados atuais do arquivo de forma organizada.
-   **Edição Guiada**: Um assistente interativo pergunta quais campos você deseja alterar (Título, Autor, Assunto, Palavras-chave).
-   **Operação Segura**: Nunca modifica o arquivo original. Em vez disso, salva uma nova cópia com o sufixo `_modificado`.
-   **Uso Intuitivo**: Basta arrastar e soltar o arquivo no terminal para começar.
-   **Validação Imediata**: Após a alteração, o script lê e exibe os metadados do novo arquivo para confirmação instantânea.

## 🔧 Pré-requisitos

Para executar este script, você precisará ter:

-   **Python 3** instalado em seu sistema.
-   A biblioteca **`pikepdf`**.

## 🚀 Instalação

1.  Clone ou faça o download do repositório contendo o script.
2.  Abra o terminal ou prompt de comando.
3.  Navegue até o diretório onde você salvou o arquivo.
4.  Instale a dependência necessária com o seguinte comando:

    ```bash
    pip install pikepdf
    ```

## 💡 Como Usar

1.  Com o terminal aberto no diretório do projeto, execute o script:

    ```bash
    python seu_script.py
    ```
    *(substitua `seu_script.py` pelo nome real do arquivo)*

2.  O programa solicitará o caminho do arquivo PDF. Você pode **colar o caminho completo** ou simplesmente **arrastar o arquivo PDF da sua pasta para a janela do terminal** e pressionar Enter.

3.  Os metadados atuais serão exibidos.

4.  Responda `sim` para a pergunta se deseja alterar os metadados.

5.  Siga as instruções, preenchendo os novos valores para cada campo. Se não quiser alterar um campo específico, apenas **pressione Enter para deixá-lo em branco**.

6.  Confirme o nome do arquivo de saída sugerido ou digite um novo caminho completo.

## 🛠️ Como o Código Funciona

O script é construído em torno de duas bibliotecas principais:

-   **`pikepdf`**: A biblioteca central para toda a manipulação de PDF. Ela é usada para abrir o arquivo, acessar o dicionário de informações (`docinfo`) para ler e escrever metadados, e salvar o novo arquivo de forma segura.
-   **`os`**: Utilizada para interações com o sistema operacional, como verificar se um arquivo existe (`os.path.exists`) e manipular caminhos de arquivo de forma inteligente (`os.path.split`, `os.path.join`) para sugerir um nome de saída conveniente.

## 📄 Licença

Este projeto é de código aberto e pode ser modificado e distribuído livremente.
