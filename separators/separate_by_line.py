from utils.arquivo import obter_cabecalho, get_file_lines, contagem_separacao

import os 


def linha_separar(dict_separantion):
    try:
        linhas_arquivo = get_file_lines(dict_separantion['caminho_origem'])
        cabecalho = obter_cabecalho(dict_separantion['cabecalho'], dict_separantion['caminho_origem'])
        linhas_arquivo = linhas_arquivo[1:]
        total_linhas = len(linhas_arquivo)
        if total_linhas <= dict_separantion['por_linhas']:
            return contagem_separacao(
                dict_separantion,
                cabecalho,
                linhas_arquivo,
                total_linhas
            )

        inicio = 0
        fim_linha = dict_separantion['por_linhas']
        numero_partes = 1
        while inicio < total_linhas:
            nome_parte = f"parte_{numero_partes}.csv"
            caminho_saida = os.path.join(dict_separantion['caminho_destino'], nome_parte)
            with open(caminho_saida, 'w', encoding='cp1252') as f:
                f.write(cabecalho + '\n')
                f.writelines(linhas_arquivo[inicio:fim_linha])

            inicio = fim_linha
            fim_linha += dict_separantion['por_linhas']
            numero_partes += 1

        return True

    except Exception as e:
        print(f"Erro ao processar: {e}")
        return False




