# > FUNÇÕES

# Funções que já utilizei

"""
print() # - Imprimi uma mensagem (int, float, str) no console (terminal, cmd)
input() # - Retorna um dado informado pelo usuário (entrada padrão) e pode receber uma string
len() # - Recebe uma lista e retorna o tamanho dessa lista
max() # - Retorna o maior valor de uma lista
"""

# Criação de Funções

# Função inicial

def linguagem():
    print('Linguagem Python')

linguagem()

# Função com parâmetros

def saudacao(nome, lingua):
    print(f'Seja bem-vinda(o), {nome}!')
    print(f'Linguagem: {lingua}')

saudacao('David', 'Python')

# Função com parâmetro default

def saudacao(nome, lingua='C++'):
    print(f'Seja bem-vinda(o), {nome}!')
    print(f'Linguagem: {lingua}')

saudacao('Giovana')

# Funções com retorno

def soma(num1, num2):
    return num1 + num2
resultado = soma(5,7)

print('O resultado da soma é', resultado)