from time import sleep
numero = 1
adicao = 1
subtracao = 1
divisao = 1
multiplicacao = 1
print("Selecione qual operação ser calculada")
print("\033[1m1-Adição | 2-Subtração | 3-Divisão: | 4-Multiplicação\033[m")
selecao = int(input("Qual a sua escolha:"))
if selecao == 1:
    while adicao <= 10:
        numero = 1
        while numero <= 10:
            print(f"{adicao} + {numero} = {adicao + numero}")
            numero += 1
        adicao += 1
        sleep(1)
        print(end='\n')
if selecao == 2:
    while subtracao <= 10:
        numero = 1
        while numero <= 10:
            print(f"{subtracao} - {numero} = {numero - subtracao}")
            numero += 1
        subtracao += 1
        sleep(1)
        print(end='\n')
if selecao == 3:
    while divisao <= 10:
        numero = 1
        while numero <= 10:
            print(f"{divisao} ÷ {numero} = {divisao / numero:.2f}")
            numero += 1
        divisao += 1
        sleep(1)
        print(end='\n')
if selecao == 4:
    while multiplicacao <= 10:
        numero = 1
        while numero <= 10:
            print(f"{multiplicacao} x {numero} = {multiplicacao * numero}")
            numero += 1
        multiplicacao += 1
        sleep(1)
        print(end='\n')
else:
   print("\033[1mFINALIZADO!\033[m")
if selecao >= 5:
    print("\033[1;31mDigite a seleção correta\033[m")


