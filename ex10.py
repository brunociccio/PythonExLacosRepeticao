'''
4 - Dados dois numeros que representam um intervalo, exibir os numeros multiplos de 5 deste intervalo.
---------------------
Inicio: 12
Fim: 34
Mult 5: 15 20 25 30
----------------------
'''
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
mult5 = n1
while mult5 <= n2:
    if mult5 % 5 == 0:
        print(mult5, end=" ")
    mult5 += 1