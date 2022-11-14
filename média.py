x = 3
soma = 0
while x <= 5:
    numero = int(input(f"{x} Digite o número:"))
    soma = soma + numero
    x = x + 1
print(f"Média: {soma / 3:.2f}")