nome = input("Nome de Usuário; ")
senha = input("Senha de Usuário: ") 


nome_bd = "Pedro"
senha_bd = "040102004"

if nome_bd == nome and senha_bd == senha:
   print("Login Efetuado...")
else:
    print("Credenciais erradas!")