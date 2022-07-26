# A imobiliária XYZ vende apenas terrenos retangulares. Faça um programa para ler as dimensões de um 
# terreno e exibir a área do mesmo.

print("Digite a dimensão do seu terreno")

lado = float(input("Digite o tamanho do lado do seu terreno: "))
comp = float(input("Digite o tamanho do comprimento do seu terreno: "))

calc = comp * lado 

print("Você tem {:.2f} de área no seu terreno".format(calc))

