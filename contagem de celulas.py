valor = float(input("Digite o valor a pagar: R$"))
cedulas = 0
atual = 100
apagar = valor
moeda = "cédulas(s)"
while True:
    if atual <= apagar:
        apagar -= atual
        cedulas += 1
    else:
        print(f"{cedulas} {moeda} de R${atual}")
        if apagar == 0:
            break
        if atual == 100:
            atual = 50
        if atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 2
        elif atual == 2:
            atual = 1
            moeda = "moedas(s)"
        elif atual == 1:
            atual = 0.50
            moeda = "moedas(s)"
        elif atual == 0.50:
            atual = 0.25
            moeda = "moedas(s)"
        elif atual == 0.25:
            atual = 0.10
            moeda = "moedas(s)"
        elif atual == 0.10:
            moeda = "moedas(s)"
            atual = 0.05
            print("1 moeda(s) de 0,05")
            break
        cedulas = 0

