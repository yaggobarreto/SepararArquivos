# 📂 SepararArquivos

Ferramenta desenvolvida em Python para realizar a separação automática de arquivos CSV de grande volume.

O sistema permite dividir arquivos de duas formas:

* **Por quantidade de linhas**
* **Por valor de uma coluna específica**

Essa abordagem facilita o processamento, análise e distribuição de grandes arquivos em partes menores e mais gerenciáveis.

---

# 🚀 Funcionalidades

## Separação por linhas

Divide um arquivo CSV em múltiplos arquivos menores com uma quantidade fixa de registros por arquivo.

### Exemplo

Arquivo original:

```csv
id;nome
1;João
2;Maria
3;José
4;Ana
5;Carlos
```

Configuração:

```text
1000 linhas por arquivo
```

Resultado:

```text
parte_1.csv
parte_2.csv
parte_3.csv
...
```

---

## Separação por coluna

Cria arquivos distintos com base nos valores encontrados em uma determinada coluna.

### Exemplo

Arquivo original:

```csv
cliente;valor
BANCO_A;100
BANCO_B;200
BANCO_A;300
BANCO_C;150
```

Resultado:

```text
BANCO_A.csv
BANCO_B.csv
BANCO_C.csv
```

Cada arquivo conterá apenas os registros referentes ao valor correspondente da coluna selecionada.

---

# 🏗️ Estrutura do Projeto

```text
SepararArquivos/
│
├── main.py
│
├── connectionDB/
│   └── my_mysql.py
│
├── separators/
│   ├── separate_by_line.py
│   └── separate_by_colunm.py
│
├── utils/
│   ├── __init__.py
│   └── arquivo.py
│
└── README.md
```

---

# 📋 Fluxo de Execução

1. Carrega as configurações.
2. Obtém os parâmetros de separação.
3. Identifica o tipo de separação:

   * Linhas
   * Coluna
4. Processa o arquivo.
5. Gera os arquivos resultantes.
6. Atualiza o status do processamento.

---

# ⚙️ Tecnologias Utilizadas

* Python 3.x
* python-dotenv
* Manipulação de arquivos CSV
* MySQL (configuração de processamento)

---

# 📦 Instalação

Clone o projeto:

```bash
git clone https://github.com/yaggobarreto/SepararArquivos.git
```

Acesse a pasta:

```bash
cd SepararArquivos
```

Crie um ambiente virtual:

```bash
python -m venv venv
```

Ative o ambiente:

### Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Instale as dependências:

```bash
pip install python-dotenv
```

---

# ▶️ Executando o Projeto

```bash
python main.py
```

---

# 📝 Configurações

O sistema utiliza variáveis de ambiente carregadas através do arquivo `.env`.

Exemplo:

```env
CAMINHO_ORIGEM=C:\Arquivos\entrada.csv
CAMINHO_DESTINO=C:\Arquivos\saida
```

---

# 🔍 Principais Módulos

## main.py

Responsável por:

* Inicializar a aplicação
* Carregar configurações
* Direcionar o processamento

---

## separate_by_line.py

Responsável por:

* Ler o arquivo
* Dividir por quantidade de linhas
* Gerar arquivos numerados

Exemplo:

```text
parte_1.csv
parte_2.csv
parte_3.csv
```

---

## separate_by_colunm.py

Responsável por:

* Identificar valores únicos de uma coluna
* Criar um arquivo para cada valor encontrado

Exemplo:

```text
CLIENTE_A.csv
CLIENTE_B.csv
CLIENTE_C.csv
```

---

## utils/arquivo.py

Funções auxiliares para:

* Leitura de arquivos
* Obtenção de cabeçalhos
* Contagem de registros
* Tratamento de valores

---

# 🛡️ Tratamento de Erros

O projeto possui tratamento básico de exceções para:

* Arquivos inexistentes
* Erros de leitura
* Problemas na geração dos arquivos
* Falhas durante o processamento

---

# 📈 Possíveis Melhorias Futuras

* Interface gráfica
* Logs estruturados
* Processamento paralelo
* Suporte a XLSX
* Configuração via API
* Dashboard de monitoramento
* Testes automatizados
* Dockerização

---

# 👨‍💻 Autor

Yago Barreto

GitHub:
https://github.com/yaggobarreto

---

# 📄 Licença

Projeto desenvolvido para automação e processamento de arquivos.

Uso livre para estudos e adaptações.
