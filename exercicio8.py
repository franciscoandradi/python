numero1 = int(input("Digite um numero: "))
numero2 = int(input("Digite o segundo numero: "))

print("quantas vezes você quer parcelar? ")
opcao = input(
            "Escolha uma opção:\n"
            "/ = Divisao\n"
            "* = Multiplicacao\n"
            "+ = Somar\n"
            "- = Subtrair\n"
            "Opção: "
    )

if opcao == "+":
            print ("Valor Somado: ", numero1 + numero2)            
elif opcao == "-":
            print ("Valor Subtraído: ", numero1 - numero2)
elif opcao == "*":
            print ("Valor Multiplicado: ", numero1  * numero2)
elif opcao == "/":
            if numero2 == 0:
                print("Erro: divisão por zero!")
            else:
                print ("Valor Dividido ", numero1  / numero2)

else:
        print("escolha uma opção que existe\n")

