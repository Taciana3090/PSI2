# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros 
# quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros 
# quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a 
# quantidades de latas de tinta a serem compradas e o preço total.

print(" ---------- LOJA DE TINTAS -------------")

tam = input("Qual o tamanho da área em metros quadrados que será pintada: ")
litros = float(tam) / 3

preco = 80.0
capacidadeL = 18

latas = litros / capacidadeL
total = latas * preco

print(f'Você usará {latas:.2} latas')
print(f'O preço total de tintas necessárias será de {total}')
