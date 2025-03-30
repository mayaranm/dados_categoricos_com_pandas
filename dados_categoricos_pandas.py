import pandas as pd
import numpy as np

# Criando uma serie de dados categoricos
altura = pd.Series(["alto", "médio", "alto", "baixo", "médio", "alto"], dtype="category")

# Exibindo a serie categorica
print("Série categórica (Altura):")
print(altura)

# Contando a quantidade de cada categoria
contagem_altura = altura.value_counts()
print("\nContagem de cada categoria:")
print(contagem_altura)

# Criando uma serie de dados numéricos para comparar com as alturas
notas = pd.Series([8, 7, 9, 5, 6, 10])

# Realizando uma comparação entre as notas e categorizando as alturas em função da nota
resultado = pd.DataFrame({
    'Altura': altura,
    'Nota': notas,
    'Nota Alta': notas > 7
})

print("\nDataFrame com comparação de notas e alturas:")
print(resultado)
