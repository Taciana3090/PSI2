# Ler o valor de um cheque e escrever o quanto vai ser recolhido de CPMF. Considere que imposto recolhe uma 
# taxa de 0,3%. Imprimir o valor do imposto.
cheque = input("Digite o valor do seu cheque:")
imposto = float(cheque) * 0.003
print(f'O valor do imposto recolhido foi {imposto}')