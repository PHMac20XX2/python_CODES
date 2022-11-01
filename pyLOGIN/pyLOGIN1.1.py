nome = input("Nome de Usuário; ")
qtd_name = len(nome)
senha = input("Senha de Usuário: ") 
qtd_pass = len(senha)

nome_bd = "Pedro"
senha_bd = "040102004"

if nome_bd == nome and senha_bd == senha:
   print("Login Efetuado...")
else:
    print("Credenciais erradas!")