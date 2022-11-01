nome = str(input ('Digite seu nome: '))
idade = int(input ('Digite sua idade: '))
altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
ano = int(input ('Em qual ano estamos?: '))

# Calcúlos Gerais
ano_Nasc = ano - idade
imcV = peso / (altura ** 2)

print (100*'-')

print (f'O {nome} tem {idade} anos, sua altura é de {altura} cm.')
print (f'Seu IMC é de {imcV:.1f}')
print ('Seu Ano de Nascimento é em {}'.format(ano_Nasc))

print (100*'-')

if imcV <= 18.5:
    print('Você está abaixo do peso normal')
elif imcV <= 24.9:
    print ('Você está com o peso normal')
elif imcV <= 29.9:
    print ('Você está acima do peso')
    