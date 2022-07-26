# Ler a temperatura de uma pessoa e exibir a mensagem “Febre Alta” (temp ≥ 39), 
# “Febril”(39 > temp ≥ 37) ou “Sem Febre” (temp < 37).

tem = float(input("Digite a sua temperatura: "))
if tem >= 39:
    print("Febre alta")
elif tem  < 39 and tem >= 37:
    print('Febril')
else:
    print("Sem febre")