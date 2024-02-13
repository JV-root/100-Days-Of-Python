'''
Comece executando as instruções de atribuição:

>>> s1 = 'ant'
>>> s2 = 'bat'
>>> s3 = 'cod'
            
Escreva expressões Python usando s1, s2 e s3 e os operadores + e * a fim de
avaliar para:  

'ant bat cod'
'ant ant ant ant ant ant ant ant ant ant'
'ant bat bat cod cod cod'
'ant bat ant bat ant bat ant bat ant bat ant bat ant bat'
'batbatcod batbatcod batbatcod batbatcod batbatcod'

'''

s1 = 'ant'
s2 = 'bat'
s3 = 'cod'

# 'ant bat cod'
expressao1 = s1 + ' ' + s2 + ' ' + s3
print(expressao1)

# 'ant ant ant ant ant ant ant ant ant ant'
expressao2 = 10 * (s1 + ' ')
print(expressao2)

# 'ant bat bat cod cod cod'
expressao3 = s1 + ' ' + 2 * (s2 + ' ') + 2 * (s3 + ' ')
print(expressao3)

# 'ant bat ant bat ant bat ant bat ant bat ant bat ant bat'
expressao4 = 7 * (s1 + ' ' + s2 + ' ')
print(expressao4)

# 'batbatcod batbatcod batbatcod batbatcod batbatcod'
expressao5 = 5 * (s2 + s3 + ' ')
print(expressao5)