login = "admin"
senha = "admin"

tentativas = 3



while tentativas > 0:
    loginuser = input("Qual é o login: ")
    senhauser = input("Qual é a senha: ")

    if loginuser == login and senhauser == senha:
        print("Login EFETUADO")
        break
    else: 
        tentativas = tentativas -1
        print("senha errada seu merda")    
if tentativas == 0:
    print("se foder")
