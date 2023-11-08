import re

# Ler o conteúdo do arquivo JSON
with open('Character.json', 'r') as file:
    json_data = file.read()

# Corrigir a formatação adicionando vírgulas entre objetos
json_data = re.sub(r'}\s*{', '},\n{', json_data)

# Escrever o JSON corrigido num novo arquivo
with open('Characters.json', 'w') as file:
    file.write(json_data)
