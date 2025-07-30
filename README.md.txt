# Projeto de Consolidação e Análise de Dados de E-commerce

Este projeto demonstra um pipeline completo de consolidação e análise de dados de um e-commerce fictício, utilizando Python e a biblioteca Pandas em um ambiente Jupyter Notebook. O objetivo principal é simular um cenário de negócio real onde dados de diferentes fontes (clientes, produtos e pedidos) precisam ser integrados, limpos e processados para gerar insights valiosos e suportar tomadas de decisão.

## Funcionalidades e Objetivos

* **Geração de Dados Fictícios:** Criação de conjuntos de dados realistas (clientes, produtos, pedidos) para simular um cenário de e-commerce.
* **Exploração de Dados:** Análise inicial das estruturas, tipos de dados e qualidade dos dados brutos.
* **Consolidação de Dados:** Combinação de múltiplas fontes de dados em um único conjunto de dados coerente para facilitar a análise.
* **Análise Descritiva:** Extração de métricas e padrões-chave sobre vendas, clientes e produtos.
* **Visualização de Dados:** Apresentação de insights através de gráficos e tabelas para uma compreensão clara.

## Estrutura do Projeto

A organização do projeto segue as melhores práticas para pipelines de dados e desenvolvimento de notebooks:

ecommerce_data_consolidation/
├── data/
│   ├── raw/              # Contém os arquivos CSV brutos (clientes, produtos, pedidos)
│   └── processed/        # Armazena o conjunto de dados consolidado após o processamento
├── notebooks/
│   ├── 01_gerar_dados.ipynb              # Notebook para geração dos dados fictícios (opcional, se os CSVs já existirem)
│   ├── 02_exploracao_e_consolidacao.ipynb # Notebook principal para carregar, explorar e consolidar os dados
│   └── 03_analise_e_visualizacao.ipynb   # Notebook para análises aprofundadas e visualizações
├── scripts/
│   └── gerador_dados_ecommerce.py # Script Python autônomo para geração de dados
├── README.md             # Este arquivo de descrição do projeto
└── requirements.txt      # Lista de dependências Python do projeto


## Tecnologias Utilizadas

* **Python 3.x**
* **Pandas**: Biblioteca essencial para manipulação e análise de dados.
* **NumPy**: Suporte a operações numéricas de alto desempenho.
* **Jupyter Notebook**: Ambiente de computação interativa para desenvolvimento, documentação e apresentação de código.
* **Matplotlib / Seaborn**: Bibliotecas para criação de visualizações de dados.

## Como Executar o Projeto Localmente

Para rodar este projeto em sua máquina, siga os passos abaixo:

1.  **Clone o Repositório:**
    ```bash
    git clone https://github.com/BrunoBDados/ecommerce_data_consolidation.git
    cd ecommerce_data_consolidation
    ```

2.  **Crie e Ative um Ambiente Virtual (Recomendado):**
    É uma boa prática isolar as dependências do projeto.
    ```bash
    python -m venv venv
    # No Windows
    .\venv\Scripts\activate
    # No macOS/Linux
    source venv/bin/activate
    ```

3.  **Instale as Dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Gere ou Posicione os Dados Brutos:**
    * **Opção A (Gerar):** Execute o script Python `gerador_dados_ecommerce.py` para criar os CSVs. Eles serão salvos em `data/raw/`.
        ```bash
        python scripts/gerador_dados_ecommerce.py
        ```
    * **Opção B (Usar Existente):** Se você já possui os arquivos `clientes.csv`, `produtos.csv` e `pedidos.csv`, certifique-se de que eles estão na pasta `data/raw/`.

5.  **Inicie o Jupyter Notebook:**
    A partir da pasta **raiz do projeto** (`ecommerce_data_consolidation/`) no seu terminal:
    ```bash
    jupyter notebook
    ```
    Isso abrirá a interface do Jupyter em seu navegador.

6.  **Execute os Notebooks:**
    No navegador, navegue até a pasta `notebooks/` e execute os notebooks na ordem:

    * **`01_gerar_dados.ipynb`**: (Opcional, se você usou a Opção B no passo 4) Para ver o código de geração de dados.
    * **`02_exploracao_e_consolidacao.ipynb`**: Execute as células para carregar, explorar e consolidar os dados. Este notebook salvará o arquivo `dados_ecommerce_consolidados.csv` na pasta `data/processed/`.
    * **`03_analise_e_visualizacao.ipynb`**: Execute as células para realizar análises e visualizar os insights a partir dos dados consolidados.

## Insights e Resultados (Exemplos - Atualize com seus próprios achados!)

* **Desempenho de Vendas:** Identificação de picos de vendas por período e tendências sazonais.
* **Clientes de Alto Valor:** Análise dos clientes que mais contribuem para a receita.
* **Categorias de Produtos Populares:** Quais categorias de produtos geram mais vendas ou lucro.
* **Distribuição Geográfica de Clientes:** Origem dos clientes e volume de pedidos por país.

*(Recomenda-se adicionar capturas de tela dos gráficos gerados nos notebooks aqui para um portfólio mais visual!)*

## Contribuições

Sinta-se à vontade para abrir [issues](https://github.com/BrunoBDados/ecommerce_data_consolidation/issues) para relatar bugs ou sugerir melhorias, ou enviar [pull requests](https://github.com/BrunoBDados/ecommerce_data_consolidation/pulls) com novas funcionalidades.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Autor

**Bruno Heleno Barbosa**
[Perfil no GitHub](https://github.com/BrunoBDados)
