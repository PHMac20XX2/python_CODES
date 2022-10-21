print ('  - IMC / IDADE / NOME - ')
print (100 * '-')

nome = input ('Digite seu nome: ')
idade = int (input ('Digite sua idade: '))
altura = float (input ('Digite sua altura: '))
peso = float (input ('Digite seu peso: '))    
imcV = peso / (altura ** 2)
ano = 2022
ano_Nasc = ano - idade


print (100 * '-')
print (f'O {nome} tem {idade} anos, sua altura é de {altura} cm.')

print (100 * '-')
print (f'Seu IMC é de {imcV:.2f}')

print (100 * '-')
print ('Seu Ano de Nascimento é em {}'.format(ano_Nasc))
print (100 * '-')