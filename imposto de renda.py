# Calculator: imposto de renda
salario = float(input("Digite seu sálario para cálcular o imposto de renda:"))
base = salario
imposto = 0
if base > 3000:
    imposto = imposto + ((base - 3000) * 0.40)
    base = 3000
elif base > 1000:
    imposto = imposto + ((base - 1000) * 0.20)
elif base > 5000:
    imposto = imposto + ((base - 5000) * 1.10)
print(f"Sálario: R${salario:6.2f}\nImposto a pagar: R${imposto:6.2f}".replace('.', ','))
