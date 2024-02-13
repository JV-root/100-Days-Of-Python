'''
Traduza os comandos a seguir para expressões Booleanas em Python e avalie-as:


A soma de 2 e 2 é menor que 4.
O valor de 7 // 3 é igual a 1 + 1.
A soma de 3 ao quadrado e 4 ao quadrado é igual a 25.
A soma de 2, 4 e 6 é maior que 12.
1387 é divisível por 19.
31 é par. (Dica: o que o resto lhe diz quando você divide por 2?)
O preço mais baixo dentre R$ 34,99, R$ 29,95 e R$ 31,50 é menor que R$ 30,00.*

'''

# A soma de 2 e 2 é menor que 4.
soma = 2 + 2
comparacao = soma < 4
print(f'A soma de 2 e 2 é menor que 4? \n {comparacao}')

# O valor de 7 // 3 é igual a 1 + 1.
divisao = 7 // 3
comparacao = divisao == 1 + 1
print(f'O valor de 7 // 3 é igual a 1 + 1? \n {comparacao} \n ')

# A soma de 3 ao quadrado e 4 ao quadrado é igual a 25.
soma = 3 ** 2 + 4 ** 2
comparacao = soma == 25
print(f'A soma de 3 ao quadrado e 4 ao quadrado é igual a 25? \n {comparacao} \n ')

# A soma de 2, 4 e 6 é maior que 12.
soma = 2 + 4 + 6
comparacao = soma > 12
print(f'A soma de 2, 4 e 6 é maior que 12? \n {comparacao} \n ')

# 1387 é divisível por 19.
divisao = 1387 % 19
comparacao = divisao == 0
print(f'1387 é divisível por 19? \n {comparacao} \n ')

# 31 é par?
resto = 31 % 2
comparacao = resto == 0
print(f'31 é par? \n {comparacao} \n ')


# O preço mais baixo dentre R$ 34,99, R$ 29,95 e R$ 31,50 é menor que R$ 30,00.
preco1 = 34.99
preco2 = 29.95
preco3 = 31.50

menor_preco = min(preco1, preco2, preco3)
comparacao = menor_preco < 30
print(f'O menor preço é menor que R$ 30,00? \n {comparacao} \n ')