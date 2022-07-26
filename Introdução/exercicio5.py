# Faça um programa para ler o salário de um funcionário e aumentá-lo em 20%. Imprima seu salário final.
sal = float(input("Digite o seu salário: "))
aum = 0.20
salF = (sal + (sal*aum))
print(f"Seu salário era {sal}. Com o aumento foi para {salF}")