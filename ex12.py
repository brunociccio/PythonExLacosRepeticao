'''
6 - Dado um numero, informar se ele é primo ou não (primo é aquele numero divisivel somente por 1 e ele mesmo)
---------------------
Numero: 10
10 não é Primo
----------------------
---------------------
Numero: 17
17 é Primo
'''

num = int(input("Digite um número: "))
for i in range(2, num//2 + 1):
    if num % i == 0:
        print(num, "não é primo!")
        break
else:
    print(num, "é primo!")