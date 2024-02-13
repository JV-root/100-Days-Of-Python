'''
Escreva expressões algébricas Python correspondentes aos seguintes comandos:  

A soma dos 5 primeiros inteiros positivos.
A idade média de Sara (idade 23), Mark (idade 19) e Fátima (idade 31).
O número de vezes que 73 cabe em 403.
O resto de quando 403 é dividido por 73.
2 à 10ª potência.
O valor absoluto da distância entre a altura de Sara (54 polegadas) e a
altura de Mark (57 polegadas).
O menor preço entre os seguintes preços: R$ 34,99, R$ 29,95 e R$ 31,50.


'''


# A soma dos 5 primeiros inteiros positivos.
soma = 1 + 2 + 3 + 4 + 5
print(f'A soma dos 5 primeiros números inteiros positivos é: {soma}')


# A idade média de Sara (idade 23), Mark (idade 19) e Fátima (idade 31).
sara = 23
mark = 19
fatima = 31

media = (sara + mark + fatima) / 3

print(f'A idade média de Sara, Mark e Fátima é: {media}')

# O número de vezes que 73 cabe em 403.
divisao = 403 // 73
print(f'O número 73 cabe em 403 {divisao} vezes.')

# O resto de quando 403 é dividido por 73.
resto = 403 % 73
print(f'O resto de 403 dividido por 73 é: {resto}')


# 2 à 10ª potência.
potencia = 2 ** 10
print(f'2 à potência de 10 é: {potencia}')


# O valor absoluto da distância entre a altura de Sara (54 polegadas) e a altura de Mark (57 polegadas).
sara = 54
mark = 57

distancia = abs(sara - mark)
print(f'O valor absoluto da distância entre a altura de Sara e a altura de Mark é: {distancia}')

# O menor preço entre os seguintes preços: R$ 34,99, R$ 29,95 e R$ 31,50.
preco1 = 34.99
preco2 = 29.95
preco3 = 31.50

menor_preco = min(preco1, preco2, preco3)
print(f'O menor preço é: {menor_preco}')

