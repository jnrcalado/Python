# Repetição com tamanho fixo da lista
lista = [1, 2, 3]
x = 0
while x < 3:
    print(lista[x])
    x += 1

# Repetição com tamanho da lista usando (len)
lista = [1, 2, 3]
x = 0
while x < len(lista):
    print(lista[x])
    x += 1

# Adição de elementos
L = ["a"]           # forma simplificada
L.append("a")       # forma extensa
L
['a']
L.append("b")
L
['a', 'b']
L.append("c")
L
['a', 'b', 'c']
len(L)
3
# Adição de elementos á lista
lista = []
while True:
    n = int(input("Digite um número (0 sair):"))
    if n == 0:
        break
    lista.append(n)
x = 0
while x < len(L):
    print(L[x])
    x += 1
