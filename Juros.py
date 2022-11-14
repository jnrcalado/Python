# Valor do depósito incial
# Taxa de juros
from time import sleep
mes = 1
taxajuros = 0.65
depositoinicial = float(input("Valor inicial do depósito: R$"))
while mes <= 2:
    print(f"Janeiro: R$ {depositoinicial * taxajuros:.2f}".replace('.', ','))
    print(f"Fevereiro: R$ {depositoinicial * taxajuros:.2f}".replace('.', ','))
    print(f"Marcio: R$ {depositoinicial * taxajuros:.2f}".replace('.', ','))
    print(f"Abril: R$ {depositoinicial * taxajuros:.2f}".replace('.', ','))
    print(f"Maio: R$ {depositoinicial * taxajuros:.2f}".replace('.', ','))
    print(f"Junho: R$ {depositoinicial * taxajuros:.2f}".replace('.', ','))
    print(f"Julho: R$ {depositoinicial * taxajuros:.2f}".replace('.', ','))
    print(f"Agosto: R$ {depositoinicial * taxajuros:.2f}".replace('.', ','))
    print(f"Setembro: R${depositoinicial * taxajuros:.2f}".replace('.', ','))
    print(f"Outubro: R$ {depositoinicial * taxajuros:.2f}".replace('.', ','))
    print(f"Novembro: R$ {depositoinicial * taxajuros:.2f}".replace('.', ','))
    print(f"Dezembro: R$ {depositoinicial * taxajuros:.2f}".replace('.', ','))
    print("-" * 70)
    sleep(0.6)
    mes = mes + 1
valortotal = depositoinicial - (depositoinicial * 0.65)
print(f"Valor total de juros ao mês (30 dias):R$ {valortotal:.2f}".replace('.', ','))
if depositoinicial:
    quantidademes = int(input("Quantidade de meses:"))
    sleep(0.4)
    print(f"\033[1mR${quantidademes * valortotal:.2f}\033[m".replace('.', ','))




