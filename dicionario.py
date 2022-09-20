# > DICIONÁRIOS

# Criando dicionários

from operator import truediv


dicionario = {}
dicionario = dict()

dicionario = {'nome': 'David', 'idade': 23, 'altura': 1.68}

print(dicionario)
print(dicionario['idade'])

# Adicionando elementos em um dicionario

dicionario['programador'] = True

print(dicionario)

dicionario['altura'] = 2

print(dicionario)

# Iterando sobre um dicionário

for chave in dicionario:
    print(chave, dicionario[chave])

# Testando a existência de uma chave

print('peso' in dicionario)
print('altura' in dicionario)