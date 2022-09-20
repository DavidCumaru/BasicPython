# > ESTRUTURAS CONDICIONAIS

idade = 20

if idade >= 18:
    print('Você é maior de idade.')
else:
    print('Você é menor de idade.')

"""
Imagine que você queira imprimir "Aprovado", caso o estudante tenha uma média superior ou igual a 7, e "Reprovado", caso a média seja inferior a 7.
"""

media = float(input('Insere a média do estudante: '))

if media >= 7:
    print('Você foi aprovado!')
elif media >=5:
    print('Recuperação')
else:
    print('Você foi reprovado!')

media = 10
presenca = 100

if media >= 7 and presenca >= 70:
    print('Aprovado')
else:
    print('Reprovado!')
