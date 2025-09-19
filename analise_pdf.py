import pikepdf
import os


def ler_metadados(caminho_arquivo):
    """
    Lê os metadados de um arquivo PDF e os exibe de forma organizada.
    Retorna True se o arquivo for lido com sucesso, False caso contrário.
    """
    if not os.path.exists(caminho_arquivo):
        print(f"\nErro: O arquivo '{caminho_arquivo}' não foi encontrado.")
        return False

    try:
        with pikepdf.Pdf.open(caminho_arquivo) as pdf:
            print(f"\n--- METADADOS DE: {os.path.basename(caminho_arquivo)} ---")
            info = pdf.docinfo
            metadados_encontrados = 0
            for chave, valor in info.items():
                print(f"{str(chave).replace('/', ''):<15}: {valor}")
                metadados_encontrados += 1

            if metadados_encontrados == 0:
                print("Nenhum metadado encontrado no arquivo.")
            print("-------------------------------------------------")
        return True
    except Exception as e:
        print(f"\nOcorreu um erro ao ler o arquivo PDF: {e}")
        return False

def alterar_metadados(caminho_entrada, caminho_saida, novos_dados):
    """
    Altera os metadados de um PDF e salva como um novo arquivo.
    """
    try:
        with pikepdf.Pdf.open(caminho_entrada) as pdf:
            for chave, valor in novos_dados.items():
                pdf.docinfo[chave] = valor

            pdf.save(caminho_saida)
            print(f"\nSucesso! Arquivo com metadados alterados salvo em: '{caminho_saida}'")
            return True
    except Exception as e:
        print(f"\nOcorreu um erro ao salvar o arquivo: {e}")
        return False

def main():
    """
    Função principal que orquestra o fluxo do programa.
    """
    print("--- Ferramenta Interativa de Metadados de PDF ---")

    caminho_entrada = input("Arraste o arquivo PDF para o terminal ou cole o caminho completo: ").strip().strip('"')

    if not ler_metadados(caminho_entrada):
        print("\nEncerrando o programa.")
        return

    resposta = input("\nDeseja alterar esses metadados? (sim/não): ").lower().strip()

    if resposta != 'sim':
        print("\nOperação cancelada. Encerrando o programa.")
        return

    print("\n--- EDIÇÃO DE METADADOS ---")
    print("(Deixe em branco e pressione Enter para não alterar um campo)")

    novos_metadados = {}

    titulo = input("Novo Título: ").strip()
    if titulo: novos_metadados['/Title'] = titulo

    autor = input("Novo Autor: ").strip()
    if autor: novos_metadados['/Author'] = autor

    assunto = input("Novo Assunto: ").strip()
    if assunto: novos_metadados['/Subject'] = assunto

    palavras_chave = input("Novas Palavras-chave: ").strip()
    if palavras_chave: novos_metadados['/Keywords'] = palavras_chave

    if not novos_metadados:
        print("\nNenhum metadado foi alterado. Encerrando.")
        return

    diretorio, nome_arquivo = os.path.split(caminho_entrada)
    nome_base, extensao = os.path.splitext(nome_arquivo)
    sugestao_saida = os.path.join(diretorio, f"{nome_base}_modificado{extensao}")

    print(f"\nNome sugerido para o arquivo de saída: {sugestao_saida}")
    caminho_saida = input("Pressione Enter para aceitar ou digite um novo caminho completo: ").strip().strip('"')
    if not caminho_saida:
        caminho_saida = sugestao_saida

    if alterar_metadados(caminho_entrada, caminho_saida, novos_metadados):
        print("\n--- VALIDAÇÃO PÓS-ALTERAÇÃO ---")
        print("Lendo os metadados do novo arquivo para confirmação:")
        ler_metadados(caminho_saida)

    print("\nPrograma finalizado.")


if __name__ == "__main__":
    main()