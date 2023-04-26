'''
EXERCICIOS (Utilizar laços em todos):
1 - Dado um número e um multiplo, exibir o próximo multiplo a partir do numero
---------------------
Numero: 6
Multiplo: 5
Proximo multiplo: 10
----------------------
'''
n = int(input("Digite um número: "))
mult = int(input("Digite um múltiplo: "))
while i % mult == 0:
    i += 1

prox_mult = n + (mult - (n % mult))

print("O próximo multiplo é:", prox_mult)