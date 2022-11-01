
print ("CALCULADORA")

print(100 * '-')

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

ad1 = n1 + n2
mul1 = n1 * n2
sub1 = n1 - n2 
div1 = n1 / n2

opcao = int(input('''
[1] Adição
[2] Multiplicação
[3] Subtração
[4] Divisão
Escolha uma operação: '''))

if opcao == 1:
    print("Resultado (Adição): ", ad1)
elif opcao == 2:
    print ("Resultado (Multiplicação): ", mul1)
elif opcao == 3:
    print ("Resultado (Subtração): ", sub1)
elif opcao == 4:
    print ("Resultado (Divisão): ", div1)
else:
    print ("Operador invalido")