# Exercicio Python #004 - Dissecando uma Variavel

# Crie um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

valor = input('Digite algo: ')

print(f'O tipo primitivo desse valor é {type(valor)}')
print(f'Só tem espaços? {valor.isspace()}')
print(f'É um número? {valor.isnumeric()}')
print(f'É alfabético? {valor.isalpha()}')
print(f'É alfanumérico? {valor.isalnum()}')
print(f'Está em maiúsculas? {valor.isupper()}')
print(f'Está em minúsculas? {valor.islower()}')
print(f'Está capitalizada? {valor.istitle()}')
