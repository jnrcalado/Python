print("Digite um número e descubra se ele é um número primo")
numero = int(input("Qual o número de sua escolha:"))
total = 0
for contador in range(1, numero + 1):
    if numero % contador == 0:
        print(f"\033[1;36m", end="")
        total += 1
    else:
        print(f"\033[1;31m", end="")
    print(f"{contador}", end='\n\033[m')
print(f"\033[1mO Número {numero} foi divisível {total} vezes\033[m")
if total == 2:
    print("\033[1mNúmero primo\033[m")
else:
    print("\033[1mNão é primo\033[m")

