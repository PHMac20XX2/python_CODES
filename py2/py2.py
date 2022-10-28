a = 544
b = 398
c = 400
d = 25
e = 'Pedro'

if a >= 0:
    print ('Positivo') #Caso o valor seja positivo (maior que 0) exibir POSITIVO
else:
    print ('Negativo') #Caso o valor seja negativo (menor que 0) exibir NEGATIVO

#Printando CPF
print (a, b, c, sep='.', end='-')

#Type Casting
if d == 25:
    print(d, type(d), bool(d))
else:
    print ("Errado")       