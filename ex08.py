'''
2 - Dado um numero, exibir o seu fatorial: 4! = 4 . 3 . 2 . 1 = 24
---------------------
Numero: 4
Fatorial: 24

'''
n = int(input("Digite um número: "))
fatorial = 1
for volta in range(1, 0, 1):
    fatorial = fatorial * volta

print("Fatorial = ", fatorial)

