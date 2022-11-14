prato = 5
pilha = list(range(1, prato + 1))
while True:
    print(f"\nExistem {len(pilha)} pratos na pilha")
    print(f"Pilha atual: {pilha}")
    print("Digite \033[1mE\033[m para empilhar um novo prato,")
    print("ou \033[1mD\033[m para desempilhar.\n\033[1mS\033[m para sair")
    operacao = input("Digite a Operação desejada:")
    if operacao == "D":
        if len(pilha) > 0:
            lavado = pilha.pop(-1)
            print(f"Prato {lavado} lavado!")
        else:
            print("Pilha vazia! Nada para lavar.")
    elif operacao == "E":
        prato += 1           # Adicionar novo prato
        pilha.append(prato)
    elif operacao == "S":
        break
    else:
        print("\033[1mOperação Inválida! Digite apenas E, D e S.\033[m")