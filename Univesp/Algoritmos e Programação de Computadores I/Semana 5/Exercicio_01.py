"""
Traduza estas instruções condicionais em instruções if do Python:

  
Se idade é maior que 62, exiba 'Você pode obter benefícios de pensão'.
Se o nome está na lista ['Musial', 'Aaraon', 'Williams', 'Gehrig', 'Ruth'],
exiba 'Um dos 5 maiores jogadores de beisebol de todos os tempos!'.
Se golpes é maior que 10 e defesas é 0, exiba 'Você está morto…'.
Se pelo menos uma das variáveis booleanas norte, sul, leste e oeste for True,
exiba 'Posso escapar.'.


"""


idade = 63
nome = 'Musial'
golpes = 11
defesas = 0
norte = False
sul = False
leste = False
oeste = True

if idade > 62:
    print('Você pode obter benefícios de pensão')
    
if nome in ['Musial', 'Aaraon', 'Williams', 'Gehrig', 'Ruth']:
    print('Um dos 5 maiores jogadores de beisebol de todos os tempos!')
    
if golpes > 10 and defesas == 0:
    print('Você está morto…')
    
if norte or sul or leste or oeste:
    print('Posso escapar.')

