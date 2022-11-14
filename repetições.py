from time import sleep
fim = int(input("Digite o último número a imprimir:"))
x = 1
while x <= fim:
    if x % 1 == 0:
        print(x)
        x = x + 1
        sleep(0.5)
print("\033[1mVOCÊ É INCRÍVEL!!\033[m")
