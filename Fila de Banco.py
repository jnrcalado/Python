# Simulação de uma fila de branco
u = 20
fila1 = list(range(1, u - 9))
fila2 = list(range(1, u - 9))
random = fila1, fila2
while True:        # Toda vez que um laço for Verdadeiro se utiliza True, e termina quando se torna Falso, a repetição
    print(f"\nExistem {u} clientes nas filas")
    print(f"Fila 1:{fila1}\nFila 2:{fila2}")
    print(f"Digite F para adiocionar um cliente ao fim da fila,")
    print(f"ou A para realizar o atendimento. S para sair")
    o = input("1 - Fila = A\n2 - Fila = B\nOperação (F - A - B - S):")
    if o == "A":
      print(f"Fila 1 {fila1}")
    else:
        len(fila1) > 0
        atendido = fila1.pop(0)
        print(f"Cliente {atendido} atendido")
    if o == "B":
        print(f"Fila 2 {fila2}")
        if len(fila2) > 0:
            atendido = fila2.pop(0)
            print(f"Cliente {atendido} atentido")
    else:
      print("Fila vazia! Ninguém para atender.")
    if o == "F":
     u += 1  # Incrementa o ticket do novo cliente
     fila1.append(u), fila2.append(u)
    if o == "S":
        break
    else:
        print("Operação inválida! Digite apenas F, A ou S!")