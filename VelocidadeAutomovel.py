#velocidade do carro
#velocidade permitda 80 km/h
#valor cobrado por multa R$ 5 por km/h
from time import sleep
velocidade = float(input("Velocidade do veiculo em km/h:"))
multa = velocidade * 5
if velocidade >= 80:
    sleep(0.5)
    print(f'\033[1;31mVocê ultrapassou a velocidade permitida!\033[m')
    sleep(0.5)
    print(f"\033[1mMulta aplicada! Valor cobrado: R$ 5,00 por km/h\033[m")
    sleep(1)
    print(f"\033[1mValor da sua multa: R${multa:.2f}\033[m".replace('.', ','))
else:
    var = velocidade < 80
    print("\033[1mVelocidade permitida\nBom condutor continue dando otimos exemplos\nParabéns!\033[m")



