'''
3 - Dada a base e o expoente, exibir a potencia 2 . 2 . 2 . 2 = 16 | Utilizar multiplicações sucessivas
---------------------
Base: 2
Expoente: 4
Potencia: 16
'''
n = int(input("Digite um número base: "))
exp = int(input("Digite um número para expoente: "))
potencia = 1
for i in range (exp):
    potencia *= n
print("Pontencia, ", potencia)