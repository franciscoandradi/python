compra = float(input("Quanto você pagou: "))
parcelar = input("você precisa parcelar? (S ou N): ").upper()

if parcelar == "S":
    print("quantas vezes você quer parcelar? ")
    opcao = int(input(
            "Escolha uma opção:\n"
            "1 - 2x sem juros\n"
            "2 - 3x sem juros\n"
            "3 - 4x sem juros\n"
            "4 - 5x sem juros\n"
            "5 - Não quero mais parcelar, vou pagar a vista! \n"
            "Opção: "
    ))

    if opcao == 1:
            print ("Valor de cada parcela: ", compra  / 2)
    elif opcao == 2:
            print ("Valor de cada parcela: ", compra  / 3)
    elif opcao == 3:
            print ("Valor de cada parcela: ", compra  / 4)
    elif opcao == 4:
            print ("Valor de cada parcela: ", compra  / 5)
    elif opcao == 5:
         print("pagando a vista você ganhou 5% no valor de desconto!! Valor final: ", compra * 0.95)
    else:
        print("escolha uma opção que existe\n")
        

elif parcelar == "N":
    print("parabens ganhou 5% no valor de desconto!! Valor final: ", compra * 0.95)            

