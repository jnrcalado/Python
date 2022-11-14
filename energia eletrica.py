from time import sleep
print("\033[1mPreço por tipo de consumo\033[m\n"
      "Residencial\nAté 500 = R$ 0,40\n"
      "Acima de 500 R$ 0,65\n")
print("Comercial\nAté 1000 = R$ 0,55\n"
      "Acima de 1000 = R$ 0,60\n")
print("Industrial\nAté 5000 = R$ 0,55\n"
      "Acima de 5000 = R$ 0,60\n")
sleep(1)
tipo = int(input("Tipos de instalação\n1 - Residencial\n2 - Comercial\n3 - Industrial\nQual o seu tipo:"))
print("-" * 60)
quantidade = int(input("Quantidade de kWh consumida:"))
print("-" * 60)
residencial = 1
comercial = 2
industrial = 3
if tipo == 1:
    print("Você escolheu Residencial")
    sleep(0.8)
    if quantidade <= 500:
      valorr = quantidade * 0.40
      print(f"Valor a pagar R${valorr:.2f}".replace('.', ','))
    else:
      var = quantidade > 500
      valorr2 = quantidade * 0.65
      print(f"Valor a pagar R${valorr2:.2f}".replace('.', ','))
if tipo == 2:
    print("Você escolheu Comercial")
    sleep(0.8)
    if quantidade <= 1000:
      valorc = quantidade * 0.55
      print(f"Valor a pagar R${valorc:.2f}".replace('.', ','))
    else:
      var = quantidade > 1000
      valorc2 = quantidade * 0.60
      print(f"Valor a pagar R${valorc2:.2f}".replace('.', ','))
if tipo == 3:
    print("Você escolheu Industrial")
    sleep(0.8)
    if quantidade <= 5000:
        valori = quantidade * 0.55
        print(f"Valor a pagar R${valori:.2f}".replace('.', ','))
    else:
        var = quantidade > 5000
        valori2 = quantidade * 0.60
        print(f"Valor a pagar R${valori2:.2f}".replace('.', ','))
elif tipo > 4:
    sleep(0.6)
    print("Opção Inválida!")
