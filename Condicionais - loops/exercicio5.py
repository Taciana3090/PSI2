# Faça um Programa que leia três números e mostre-os em ordem decrescente.

num1 = int(input("Digite um número:"))
num2 = int(input("Digite um número:"))
num3 = int(input("Digite um número:"))

maior = num1
if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3

menor = num1

if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3
    
meio = 0

if num1 != maior and num1 != menor:
    meio = num1
if num2 != maior and num2 != menor:
    meio = num2
if num3 != maior and num3 != menor:
    meio = num3 
    
print(f'{maior} é o número maior, {meio} é o número do meio, {menor} é o número menor.')  