primeiro_numero = int(input('Digite um número:'))
segundo_numero = int(input('Digite um número:'))
if primeiro_numero > segundo_numero:
    print("O primeiro número é maior!")
elif primeiro_numero < segundo_numero:
    print("O segundo número é maior!")
else:
    var = primeiro_numero == segundo_numero
    print("Os números são iguais!")

