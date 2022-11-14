# Aprovar empréstimo báncario
# Valor da casa a comprar - valor da casa 30% acima do salário
# Salario da pessoa
# Quantidade de anos a pagar
# Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar
valorcasa = float(input("Digite o valor da casa:R$ "))
salario = float(input("Digite o valor do seu salário:R$ "))
quantidadeanos = int(input("Digite a quantidade de anos a pagar: "))
valorprestacao = valorcasa / (quantidadeanos * 12)
salario2 = salario - (salario * 30 / 100)
if valorprestacao <= salario - (salario * 30 / 100):
    print(f"Empréstimo negado")
if valorprestacao:
    print(f"Crédito aprovado!")
    print(f"Valor da prestação mensal: R${valorprestacao:.2f}".replace('.', ','))
