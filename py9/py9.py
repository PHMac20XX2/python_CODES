print ("")
print ("   Pagamentos PHM   ")
print (50 * "-")

opcao = int (input (''' Tipos de cartão aceito
                    
 [1] Crédito:
 [2] Débito: 
 
 Digite o número do tipo de cartão: '''))

if opcao == 1:
    print ("")
    print ("Opção escolhida: Crédito")
    senha_bd = 1234
    senha = int(input ("Digite a senha: "))
print (50 * "-")
    
if senha == senha_bd:
    print (" SUA CONTA ")
else: 
    print (50 * "-")
    print ("Senha Errada")