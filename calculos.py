# Escolha qual operação deve realizar
from time import sleep

operacao = int(input('Escolha qual operação deseja realizar o calculo\n'
                     '1:Soma (+)\n2:Substração (-)\n3:Divisão (/)\n4:Multiplicação (*)\n'
                     'Digite sua operação:'))
if operacao == 1:  # Digitar os valores a ser somados
    digitevalores = int(input('\033[1mDigite os valores:\033[m'))
    digitevalores2 = int(input('\033[1mDigite os valores:\033[m'))
    sleep(0.7)
    soma = digitevalores + digitevalores2
    print(f"\033[1m{soma}\033[m")
elif operacao == 2:
    digitevalores = int(input('\033[1mDigite os valores:\033[m'))
    digitevalores2 = int(input('\033[1mDigite os valores:\033[m'))
    sleep(0.7)
    subtracao = digitevalores - digitevalores2
    print(f"\033[1m{subtracao}\033[m")
elif operacao == 3:
    digitevalores = int(input('\033[1mDigite os valores:\033[m'))
    digitevalores2 = int(input('\033[1mDigite os valores:\033[m'))
    sleep(0.7)
    divisao = digitevalores / digitevalores2
    print(f"\033[1m{divisao}\033[m")
elif operacao == 4:
    digitevalores = int(input('\033[1mDigite os valores:\033[m'))
    digitevalores2 = int(input('\033[1mDigite os valores:\033[m'))
    sleep(0.7)
    multiplicacao = digitevalores * digitevalores2
    print(f"\033[1m{multiplicacao}\033[m")
else:
    print(f"\033[1mOperação invalida digite a correta\033[m")
