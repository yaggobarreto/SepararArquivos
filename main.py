from dotenv import load_dotenv, find_dotenv
from separators import separate_by_line as linha
from separators import separate_by_colunm as coluna
from  import get_data_base_separation,set_data_base_separation




def set_form_sepration(dict_data_separation):
    if dict_data_separation['forma'] == 'coluna':
        return coluna.header_separation(dict_data_separation)

    elif dict_data_separation['forma'] == 'linhas':
        return linha.linha_separar(dict_data_separation)


def main():
    load_dotenv(find_dotenv())
    dict_data_separation = get_data_base_separation()
    if not dict_data_separation:
        print("Nenhum registro para processar.")
        return
    
    if set_form_sepration(dict_data_separation):
        set_data_base_separation(dict_data_separation['id'])



if __name__ == '__main__':
    main()

