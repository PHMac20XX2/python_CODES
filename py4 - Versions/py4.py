nome = 'Pedro'
idade = 18
altura = 1.91
peso = 86.5
imcV = peso / (altura ** 2)
ano = 2022
ano_Nasc = ano - idade

print (f'O {nome} tem {idade} anos, sua altura é de {altura} cm.')
print (f'Seu IMC é de {imcV:.2f}')
print ('Seu Ano de Nascimento é em {}'.format(ano_Nasc))
