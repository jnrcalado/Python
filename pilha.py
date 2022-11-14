T = [- 10, -8, 0, 1, 2, 5, -2, -4]
menor = T[0]
maior = T[0]
for e in T:
    if e < menor:
        menor = e
    elif e > maior:
        maior = e
print(f"{menor} e {maior}")