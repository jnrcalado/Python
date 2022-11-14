from time import sleep
codigo = 0
while True:
    codigo = int(input("Código do Produto:"))
    if codigo == 0:
        break
    quantidade = float(input("Quantidade dos Produtos:"))
    if codigo == 1:
        print(f"\033[1mValor: R${quantidade * 0.50:.2f}\033[m".replace('.', ','))
        quantidade += 1
    if codigo == 2:
        print(f"\033[1mValor: R${quantidade * 1.00:.2f}\033[m".replace('.', ','))
        quantidade += 1
        sleep(0.2)
    if codigo == 3:
        print(f"\033[1mValor: R${quantidade * 4.00:.2f}\033[m".replace('.', ','))
        quantidade += 1
        sleep(0.2)
    if codigo == 5:
        print(f"\033[1mValor: R${quantidade * 7.00:.2f}\033[m".replace('.', ','))
        quantidade += 1
        sleep(0.2)
    if codigo == 9:
        valortotal = quantidade * 8.0
        print(f"\033[1mValor: R${valortotal:.2f}\033[m".replace('.', ','))
        quantidade += 1











