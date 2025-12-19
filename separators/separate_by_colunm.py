from utils.arquivo  import get_unique_column_values
import os

def header_separation(dict_separantion):
    try:
        linhas_arquivo = get_file_lines(dict_separantion['caminho_origem'])
        header = get_header(linhas_arquivo)
        indice = get_column_index(dict_separantion,header)
        if indice <0:
            return
        
        lista_values_validat = get_unique_column_values(linhas_arquivo,indice)
        resultado = False
        for item in lista_values_validat:
            resultado = create_files(item,header,linhas_arquivo)
        return resultado
        
    except Exception as e:
        print(e)



def create_files(nome_arquivo_saida,cabecalho,linhas_original):
    try:
        caminho_completo = os.getenv('caminho_destino') + f'\\{nome_arquivo_saida}.csv' 
        linhas = []
        for linha in linhas_original:
            if nome_arquivo_saida in linha:
                linhas.append(linha)
        with open(caminho_completo, 'w', ) as arquivo_saida:
                    arquivo_saida.write(';'.join(cabecalho) + '\n')
                    for linha in linhas:
                        arquivo_saida.writelines(linha)
        return True
    except:
        return False



def get_header(linhas_arquivo)-> list:
    primeira_linha = str(linhas_arquivo[0])
    cabecalho = primeira_linha.strip().split(';')
    return cabecalho



def get_column_index(dict_separantion,header)->int:
    try:
        return int(header.index(dict_separantion['por_coluna']))
    except:
        return  -1
    


def get_file_lines(caminho_origem)->list:
    list_return = []
    with open(caminho_origem, 'r', encoding='utf-8') as f:
        for linha in f:
           list_return.append(linha)   
    return list_return



