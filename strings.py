# cálculo da média com listas
notas = [6, 7, 5, 8, 9]
soma = 0
x = 0
while x < 5:
    soma += notas[x]
    x += 1
print(f"Média: {soma / x:5.2f}")

# Cálculo da Média com notas digitadas
notas = [0, 0, 0, 0, 0, 0, 0, 0]
soma = 0
x = 1
while x < 8:
    notas[x] = float(input(f"Nota {x}:"))
    soma += notas[x]
    x += 1
x = 1
while x < 8:
    print(f"Nota {x}: \033[1m{notas[x]:<9.2f}\033[m")
    x += 1
print(f"Média \033[1m{soma / x:<7.2f}\033[m")