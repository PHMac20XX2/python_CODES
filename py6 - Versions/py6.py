num1 = input("Digite um número: ")

if num1.isnumeric():
    num1 = int(num1)
    if num1 % 2 == 0:
        print(f'{num1} é um número par!')
    else:
        print(f'{num1} é um número impar!')
else:
    print(f'O termo "{num1}" digitado nao é um número inteiro positivo!')