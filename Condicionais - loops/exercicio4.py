# Faça um Programa que peça para entrar com um ano (inteiro com 4 dígitos) e determine se o mesmo é ou não 
# bissexto (divisível por 4).
ano = input("Digite o ano: ")
ano = int(ano)
if (ano % 4 == 0) and (ano % 100 != 0):
    print(f"O ano {ano} é bissexto.")
elif  (ano % 4 == 0) and (ano % 100 == 0) and (ano % 400 == 0):
    print(f"O ano {ano} é bissexto.")
else:
    print(f'O ano {ano} não é bissexto.') 