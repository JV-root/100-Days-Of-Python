'''
Dada a lista de notas de trabalho de casa dos alunos

>>> notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]

escreva:


Uma expressão que avalia para o número de 7 notas.
Uma instrução que muda a última nota para 4.
Uma expressão que avalia para a nota mais alta.
Uma instrução que classifica as notas da lista.
Uma expressão que avalia para a média das notas.

'''


notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]

print(notas.count(7))

notas[-1] = 4

print(max(notas))


notas.sort()

print(notas)

print(sum(notas)/len(notas))