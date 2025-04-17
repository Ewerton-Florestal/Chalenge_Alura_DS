# Importar as bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib import rcParams

# Carregar os dados das lojas
loja1 = pd.read_csv("data/loja_1.csv")  # Carrega os dados da Loja 1
loja2 = pd.read_csv("data/loja_2.csv")  # Carrega os dados da Loja 2
loja3 = pd.read_csv("data/loja_3.csv")  # Carrega os dados da Loja 3
loja4 = pd.read_csv("data/loja_4.csv")  # Carrega os dados da Loja 4

# Combinar os dados em um único DataFrame para facilitar a análise
dados_juntos = pd.concat(
    [loja1, loja2, loja3, loja4], 
    keys=["Loja 1", "Loja 2", "Loja 3", "Loja 4"], 
    names=["Loja"]
)

# Avaliação inicial dos dados
dados_juntos.info()  # Exibe informações gerais sobre o DataFrame
dados_juntos.describe()  # Exibe estatísticas descritivas
dados_juntos.head(n=50)  # Exibe as primeiras 50 linhas do DataFrame

# Verificar dados faltantes
print(dados_juntos.isnull().sum())  # Conta os valores nulos em cada coluna

# Análise de faturamento por loja, já considerando o custo do frete
dados_juntos["Faturamento"] = dados_juntos["Preço"] - dados_juntos["Frete"]  # Calcula o faturamento
faturamento_por_loja = dados_juntos.groupby("Loja")["Faturamento"].sum()  # Soma o faturamento por loja
print(faturamento_por_loja)  # Exibe o faturamento por loja

# Vendas por categoria por loja
vendas_categoria = dados_juntos.groupby(["Loja", "Categoria do Produto"])["Produto"].count().unstack()  # Conta os produtos vendidos por categoria e loja
print(vendas_categoria)  # Exibe as vendas por categoria

# Média de Avaliação das lojas
avaliacoes_medias = dados_juntos.groupby("Loja")["Avaliação da compra"].mean()  # Calcula a média das avaliações por loja
print(avaliacoes_medias)  # Exibe as médias de avaliação

# Produtos Mais e Menos Vendidos por loja
produtos_vendidos = dados_juntos.groupby(["Loja", "Produto"])["Produto"].count()  # Conta os produtos vendidos por loja
produtos_mais_vendidos = produtos_vendidos.groupby("Loja").idxmax()  # Identifica o produto mais vendido por loja
produtos_menos_vendidos = produtos_vendidos.groupby("Loja").idxmin()  # Identifica o produto menos vendido por loja
print("Produtos mais vendidos por loja:")
print(produtos_mais_vendidos)  # Exibe os produtos mais vendidos
print("\nProdutos menos vendidos por loja:")
print(produtos_menos_vendidos)  # Exibe os produtos menos vendidos

# Frete médio por loja
frete_medio = dados_juntos.groupby("Loja")["Frete"].mean()  # Calcula o frete médio por loja
print(frete_medio)  # Exibe o frete médio por loja

# Visualização Gráfica

# Cores usadas para cada loja
cores = ["green", "blue", "orange", "red"]  # Define as cores para os gráficos

# Configurar fonte global para Arial e tamanho 12
rcParams['font.family'] = 'Arial'  # Define a fonte como Arial
rcParams['font.size'] = 12  # Define o tamanho da fonte como 12

# Faturamento da loja
faturamento_por_loja.plot(
    kind="bar", figsize=(8, 6), title="Faturamento por Loja", 
    ylabel="Faturamento (R$)", xlabel="Lojas Avaliadas", color=cores
)  # Cria um gráfico de barras para o faturamento
for index, value in enumerate(faturamento_por_loja):
    plt.text(index, value + 10000, f"R$ {value:,.0f}", ha="center", va="bottom", fontsize=10)  # Adiciona os valores acima das barras
plt.xticks(rotation=0)  # Mantém os rótulos do eixo X sem rotação
plt.yticks(np.arange(0, 1600000, step=100000))  # Define os ticks do eixo Y
plt.tight_layout()  # Ajusta o layout para evitar sobreposição
plt.savefig("image/faturamento.png", dpi=300)  # Salva o gráfico como imagem
plt.show()  # Exibe o gráfico

# Vendas por categoria
vendas_categoria.T.plot(
    kind="line", figsize=(12, 8), stacked=False, 
    title="Vendas por Categoria por Loja", xlabel="Categorias", ylabel="Quantidade"
)  # Cria um gráfico de linhas para as vendas por categoria
plt.legend(title="Lojas", loc="best")  # Adiciona a legenda
plt.xticks(rotation=0)  # Mantém os rótulos do eixo X sem rotação
plt.yticks(np.arange(200, 600, step=50))  # Define os ticks do eixo Y
plt.tight_layout()  # Ajusta o layout para evitar sobreposição
plt.savefig("image/vendas_categoria.png", dpi=300)  # Salva o gráfico como imagem
plt.show()  # Exibe o gráfico

# Média de Avaliação das lojas
avaliacoes_medias.plot(
    kind="barh", figsize=(8, 6), title="Média de Avaliação por Loja", 
    xlabel="Avaliação Média", ylabel="Lojas Avaliadas", color=cores
)  # Cria um gráfico de barras horizontais para as médias de avaliação
for index, value in enumerate(avaliacoes_medias):
    plt.text(value + 0.01, index, f"{value:.2f}", ha="left", va="center", fontsize=10)  # Adiciona os valores ao lado das barras
plt.tight_layout()  # Ajusta o layout para evitar sobreposição
plt.savefig("image/avaliacoes_medias.png", dpi=300)  # Salva o gráfico como imagem
plt.show()  # Exibe o gráfico

# Frete Médio
frete_medio.plot(
    kind="bar", figsize=(8, 6), title="Frete Médio por Loja", 
    ylabel="Frete Médio (R$)", xlabel="Lojas avaliadas", color=cores
)  # Cria um gráfico de barras para o frete médio
for index, value in enumerate(frete_medio):
    plt.text(index, value + 0, f"R$ {value:,.2f}", ha="center", va="bottom", fontsize=10)  # Adiciona os valores acima das barras
plt.xticks(rotation=0)  # Mantém os rótulos do eixo X sem rotação
plt.yticks(np.arange(0, 40, step=5))  # Define os ticks do eixo Y
plt.tight_layout()  # Ajusta o layout para evitar sobreposição
plt.savefig("image/frete_medio.png", dpi=300)  # Salva o gráfico como imagem
plt.show()  # Exibe o gráfico