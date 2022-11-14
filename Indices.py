n = [15, 12, 5, 7, 9]
x = 0
while x < 5:
    print(f"Número {n}\nEscolha qual posição dos números quer ser imprimida\n1 - Primeira |"
          f" 2 - Segunda | 3 - Terceira | 4 - Quarta | 5 - Quinta")
    x += 1
    break
while True:
    escolha = int(input("\033[1;31mAperte 0 se quiser sair\033[m\n"
                        "\033[1mQue posição você quer imprimir:\033[m"))
    if escolha == 0:
        break
    print(f"Você escolheu o número: {n[escolha - 1]}")
    escolha += 1
    print(f"Até mais!")
    break


