
# 📊 Análise de Vendas por Loja

Este projeto realiza uma análise exploratória de dados de vendas provenientes de quatro lojas distintas. Utilizando Python, são extraídas informações relevantes como faturamento, avaliação dos clientes, produtos mais vendidos e análise de frete, com visualizações gráficas para melhor compreensão.

## 📁 Estrutura do Projeto

```
.
├── analise_chalenge.py
├── data/
│   ├── loja_1.csv
│   ├── loja_2.csv
│   ├── loja_3.csv
│   ├── loja_4.csv
│   └── Relatorio_Final_Lojas.docx
├── image/
│   ├── faturamento.png
│   ├── vendas_categoria.png
│   ├── avaliacoes_medias.png
│   └── frete_medio.png
└── README.md
```

## 🔧 Tecnologias Utilizadas

- **Python 3**
- **Pandas** — manipulação de dados
- **Seaborn** & **Matplotlib** — visualização de dados
- **NumPy** — operações numéricas

## 📌 Funcionalidades

- 📦 Importação e consolidação dos dados de 4 lojas
- 💰 Cálculo do **faturamento líquido** por loja
- 📈 Contagem de vendas por **categoria de produto**
- ⭐ Cálculo da **média de avaliação dos clientes**
- 🛒 Identificação dos **produtos mais e menos vendidos**
- 🚚 Análise do **frete médio** por loja
- 📊 Geração de **gráficos** salvos automaticamente na pasta `image/`

## 🖼️ Exemplos de Saída Gráfica

- **Faturamento por Loja**
- **Vendas por Categoria**
- **Média de Avaliação**
- **Frete Médio**

## ▶️ Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/Ewerton-Florestal/Chalenge_Alura_DS
   cd seu-repo
   ```

2. Instale as dependências:
   ```bash
   pip install pandas matplotlib seaborn numpy
   ```

3. Certifique-se de que os arquivos `.csv` estão em `./data`.

4. Execute o script:
   ```bash
   python analise_chalenge.py
   ```

5. Os gráficos gerados estarão na pasta `./image`.

## 📂 Dados de Entrada

Cada arquivo `.csv` de loja deve conter ao menos as colunas:
- `Produto`
- `Preço`
- `Frete`
- `Categoria do Produto`
- `Avaliação da compra`

## 📌 Requisitos

- Python 3.7+
- Bibliotecas listadas acima

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 🙋‍♂️ Autor

Desenvolvido por **Ewerton Souto Pinheiro**  
📧 [LinkedIn](https://www.linkedin.com/in/ewertonpinheiroflorestal/)

---
