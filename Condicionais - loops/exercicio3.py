# Entrar com um distância (km) e o tempo de viagem (horas) de um automóvel, e dizer se a velocidade média 
# foi superior ao limite (110 km/h) ou não.
dist = float(input('Digite a distância percorrida(km): '))
tempo = float(input('Digite o tempo de viagem(horas): '))
media = dist  / tempo
if media > 110:
    print(f"A velocidade é de {media}. Você está acima da média permitida. Reduza!")
else:
    print(f'Você está em {media:.2f} por km/hr. Continue assim e uma ótima viagem.')
