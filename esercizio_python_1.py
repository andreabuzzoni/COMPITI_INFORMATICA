x = int(input('Quanti voti ha preso il 1° candidato? '))
y = int(input('Quanti voti ha preso il 2° candidato? '))
z = x+y
d = (x/z)*100
u = (y/z)*100
print('Percentuale di voti del 1° candidato: ', d, '%')
print('percentuale di voti del 2° candidato: ', u, '%')
if d>u :
    print('La vittoria è del primo candidato!')
if d<u :
    print('La vittoria è del secondo candidato!')
else :
    print('Sono pari!')                                     