'''
Escreva expressões Python correspondentes ao seguinte:

   
O comprimento da hipotenusa em um triângulo retângulo cujos dois outros lados
têm comprimentos a e b
O valor da expressão que avalia se o comprimento da hipotenusa acima é 5
A área de um disco com raio a
O valor da expressão Booleana que verifica se um ponto com coordenadas x e y está
dentro de um círculo com centro ( a, b ) e raio r

'''


import math

# O comprimento da hipotenusa em um triângulo retângulo cujos dois outros lados têm comprimentos a e b
a = 3
b = 4
c = math.sqrt(a**2 + b**2)
print(c)

# O valor da expressão que avalia se o comprimento da hipotenusa acima é 5
print(c == 5)

# A área de um disco com raio a
a = 3
area = math.pi * a**2
print(area)

# O valor da expressão Booleana que verifica se um ponto com coordenadas x e y está dentro de um círculo com centro ( a, b ) e raio r
x = 3
y = 4
a = 0
b = 0
r = 5

print((x - a)**2 + (y - b)**2 < r**2)

