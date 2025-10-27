#pandas e uma biblioteca de analise de dados em python
#A estrutura principal do pandas e o dataframe que funciona como tabela:
#linhas indexadas automaticamente começando de 0
#Colunas: "nomeadas" cada coluna pode ter um tipo de dado(int, float, string..etc)
#muito usado em ciencia de dados, planilhas, b.i e mashine larning

import pandas as pd
#criando um data frame manualmente "passando um dicionario"
#a chave do dicionario vira o nome da coluna
#a lista associada a chave vira os valores daquela coluna

df = pd.DataFrame({
    "nome": ["ana", "joao", "maria"], #coluna strin
    "idade": [25, 30, 26],            #coluna de inteiros
    "salario": [3500, 4200, 5000]     #colunas 
})

print(df) #mostra a tabela formatada
#podemos acessar uma coluna pelo seu nome como se fosse um dicionario
print("\n coluna idade:") #retorna uma series:"estrutura de coluna do pandas"
print(df["idade"])

#podemos aplicar condições pra filtrar os dados
print("exemplo mostrar quem tem salario maior que 4000:")

print(df[df["salario"] > 4000])
#retorna um novo data frame que com linhas que satisfazem a condição

#tambem podemos criar data frame apartir de uma lista de listas e expecificar os nomes das colunas manualmente

dados = [
    ["pedro",22,3100],
    ["carla",27,4700]
]

df2 = pd.DataFrame(dados, columns=["nome","idade","salario"])  #corrigido: DataFrame e columns
print("\n outro dataframe:")
print(df2)

#comcatenando data frames 
#podemos unir" concatenar varios data frames em um so"

df_total = pd.concat([df, df2], ignore_index=True)  #corrigido: df_total e ignore_index
print("\n dataframe combinado:")
print(df_total)  #corrigido: df_total ao inves de df.total
