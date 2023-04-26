'''
5 - Dados dois numeros que representam um intervalo, e um numero N que representa o multiplo, exibir os numeros
multiplos de N deste intervalo
---------------------
Inicio: 10
Fim: 47
mult: 10
Multiplos: 10 20 30 40
----------------------
'''
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
mult = int(input("Digite um número que representará um multiplo: "))
i = n1
multn = []

while i <= n2:
    if i % mult == 0:
        multn.append(i)
    i += 1
print("Multiplos: ", end=" ")
for mult in multn:
    print(mult, end=" ")