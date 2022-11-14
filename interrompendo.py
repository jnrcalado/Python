n = 0
cont = 0
while True:
    r = int(input("Digite um número:"))
    if cont == 5:
        break
    n += r
    cont += 1
print(f"Soma dos números: {n}")
print(f"Quantidade de números digitados:{cont}")
print(f"Média Aritmética:{(n + r) / cont:.1f}")


