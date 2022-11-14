from time import sleep
lista = [1, 2, 3, 4]
lista2 = [5, 6, 7, 8]
lista3 = [9, 10, 12, 13]
x = 0
while x < 1:
    print(lista)
    print(lista2)
    x += 1
sleep(1)
while x < len(lista3):
    print(lista3)
    x += 1
    break