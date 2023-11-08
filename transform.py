import pandas as pd

# Ler o DataFrame
data = pd.read_json('Characters.json')

# Verificar valores ausentes em todas as colunas
valores_ausentes = data.isna().sum()

# Exibir a contagem de valores ausentes por coluna
print(valores_ausentes)
