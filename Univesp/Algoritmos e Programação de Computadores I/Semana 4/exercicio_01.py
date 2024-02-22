'''
Implemente um programa que solicita a temperatura atual em graus Fahrenheit
do usuário e exibe a temperatura em graus Celsius usando a fórmula:

Seu programa deverá ser executado da seguinte forma:

>>>
Digite a temperatura em graus Fahrenheit: 50
A temperatura em graus Celsius é 10.0

'''




def fahrenheit_para_celsius(f):
    c = (f - 32) * 5/9
    return c

f = float(input('Digite a temperatura em graus Fahrenheit: '))

print(f'A temperatura em graus Celsius é {fahrenheit_para_celsius(f)}')

