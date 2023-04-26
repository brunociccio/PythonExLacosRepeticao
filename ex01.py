"""
Contar quantos números pares e impares foram digitados pelo usuário até
que ele digite 0
"""
# INICIO DO LAÇO
# ler os números (repetitivo)
par = 0
impar = 0
while True:
    n = int(input("Número"))
# verificar se é par ou impar (repetitivo)
    if n % 2 == 0:
        par = par + 1
    else:
        impar = impar + 1
    if n == 0:
        break
# contar os pares e os impares (repetitivo)
# FIM DO LAÇO
print(f"""
    Pares: {par}
    Impares: {impar}
""")
# exibir a quantidade de pares e impares (não repetitivo)