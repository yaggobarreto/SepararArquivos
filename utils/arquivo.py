import os 


def get_file_lines(caminho_origem)->list:
    list_return = []
    with open(caminho_origem, 'r', encoding='utf-8', errors='ignore') as f:
        for linha in f:
           list_return.append(linha)   
    return list_return



def obter_cabecalho(id_cabecalho,caminho_origem):
     cabecalho = ''         
     if id_cabecalho == 1:
          with open(caminho_origem, 'r', encoding='cp1252') as f:
            cabecalho = f.readline()          
     elif id_cabecalho == 2:
          with open(caminho_origem, 'r', encoding='cp1252') as f:
            cabecalho = f.readlines()[-1]

     return cabecalho



def contagem_separacao(dict_data_separation,cabecalho,linhas, total_linhas):
    nome_arquivo_saida = os.path.join(dict_data_separation['caminho_destino'], f"{os.path.splitext(os.path.basename(dict_data_separation['caminho_origem']))[0]}.csv")

    with open(nome_arquivo_saida, 'w', ) as arquivo_saida:
                arquivo_saida.write(cabecalho + '\n')
                arquivo_saida.writelines(linhas)
    print(f"Arquivo '{nome_arquivo_saida}' criado com {total_linhas} linhas.")
      
    return None



def remov_barras(text: str)-> str:
     if text is None:
         return ''
     return text.replace('/','').replace('\\','')


 
def get_unique_column_values(linhas_arquivo,indice)-> list:
    value_unique = set()
    for item, linha in enumerate(linhas_arquivo):
            if item == 0:
                continue
            colunas = linha.strip().split(';')
        
            colunas = [remov_barras(col) for col in colunas]
            if indice < len(colunas):
                value_unique.add(colunas[indice])
    return list(value_unique)
    