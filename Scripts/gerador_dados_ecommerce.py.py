#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Script para Geração de Dados Fictícios de E-commerce

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

# --- Configuração ---
NUM_PEDIDOS = 10000
NUM_PRODUTOS = 1000
NUM_CLIENTES = 5000
DATA_INICIO = datetime(2023, 1, 1)
DATA_FIM = datetime(2024, 12, 31)

# Definir o diretório para salvar os CSVs
# Este script assume que está sendo executado da raiz do projeto,
# ou que o diretório 'data/raw' já existe e é acessível.
output_dir = 'data/raw' # Caminho relativo à raiz do projeto
os.makedirs(output_dir, exist_ok=True)

print(f"Gerando dados e salvando em: {os.path.abspath(output_dir)}\n")

# --- Gerar Dados de Clientes ---
ids_clientes = np.arange(1, NUM_CLIENTES + 1)
nomes_clientes = [f"Cliente {i}" for i in ids_clientes]
emails_clientes = [f"cliente{i}@exemplo.com" for i in ids_clientes]
paises = ['Brasil', 'EUA', 'Canadá', 'México', 'Argentina', 'Chile', 'Colômbia', 'Peru', 'Portugal', 'Espanha']
paises_clientes = np.random.choice(paises, NUM_CLIENTES)

df_clientes = pd.DataFrame({
    'id_cliente': ids_clientes,
    'nome_cliente': nomes_clientes,
    'email_cliente': emails_clientes,
    'pais': paises_clientes
})
df_clientes.to_csv(os.path.join(output_dir, 'clientes.csv'), index=False)
print("Gerado clientes.csv")

# --- Gerar Dados de Produtos ---
ids_produtos = np.arange(1, NUM_PRODUTOS + 1)
nomes_produtos = [f"Produto {i}" for i in ids_produtos]
categorias = ['Eletrônicos', 'Roupas', 'Livros', 'Artigos para Casa', 'Esportes', 'Beleza', 'Alimentos', 'Brinquedos']
categorias_produtos = np.random.choice(categorias, NUM_PRODUTOS)
precos_produtos = np.round(np.random.uniform(5.0, 1000.0, NUM_PRODUTOS), 2)

df_produtos = pd.DataFrame({
    'id_produto': ids_produtos,
    'nome_produto': nomes_produtos,
    'categoria': categorias_produtos,
    'preco': precos_produtos
})
df_produtos.to_csv(os.path.join(output_dir, 'produtos.csv'), index=False)
print("Gerado produtos.csv")

# --- Gerar Dados de Pedidos ---
ids_pedidos = np.arange(1, NUM_PEDIDOS + 1)

# IDs de clientes aleatórios para os pedidos
ids_clientes_pedido = np.random.choice(ids_clientes, NUM_PEDIDOS)

# Datas aleatórias para os pedidos
diferenca_tempo = DATA_FIM - DATA_INICIO
dias_aleatorios = np.random.randint(0, diferenca_tempo.days, NUM_PEDIDOS)
datas_pedido = [DATA_INICIO + timedelta(days=int(d)) for d in dias_aleatorios]

# Valores totais aleatórios para os pedidos
valores_totais_pedido = np.round(np.random.uniform(10.0, 5000.0, NUM_PEDIDOS), 2)

# Associar um produto para simplicidade (em um cenário real, teria uma tabela de itens de pedido)
ids_produtos_associados_pedido = np.random.choice(ids_produtos, NUM_PEDIDOS)

df_pedidos = pd.DataFrame({
    'id_pedido': ids_pedidos,
    'id_cliente': ids_clientes_pedido,
    'data_pedido': datas_pedido,
    'valor_total': valores_totais_pedido,
    'id_produto_associado': ids_produtos_associados_pedido
})
df_pedidos.to_csv(os.path.join(output_dir, 'pedidos.csv'), index=False)
print("Gerado pedidos.csv")

print("\nTodos os arquivos CSV foram gerados com sucesso!")
print("Você deverá encontrar 'clientes.csv', 'produtos.csv' e 'pedidos.csv' no diretório 'data/raw' do seu projeto.")

