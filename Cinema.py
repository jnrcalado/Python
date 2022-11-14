lugares_vagos = [10, 2, 1, 3, 0]
print(f"Salas disponíveis: {lugares_vagos}")
while True:
    sala = int(input("Qual Sala: "))
    if sala == 0:
        print("\033[1mFIM!\033[m")
        break
    if sala > len(lugares_vagos) or sala < 1:
        print("Sala Inválida")
    elif lugares_vagos[sala - 1] == 0:
        print("Desculpe, sala lotada!")
    else:
        lugares = int(input(f"Quantos lugares você deseja ({lugares_vagos[sala - 1]} vagos):"))
        if lugares > lugares_vagos[sala - 1]:
            print("Esse número de lugares não está disponível.")
        elif lugares < 0:
            print("Número inválido")
        else:
            lugares_vagos[sala - 1] -= lugares
            print(f"{lugares} lugares vendidos")
    print("Utilização das salas")
    for x, l in enumerate(lugares_vagos):
        print(f"Sala {x + 1} - {l} Lugar(es) vazio(s)")
