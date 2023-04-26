"""
Dados 10 números pelo usuário, contar quantos são negativos e
quantos são negativos, ou nulos
"""
positivo = 0
negativo = 0
nulo = 0
for volta in range(1, 10 + 1, 1):
    n = int(input("Número: "))
    if n > 0:
        positivo = positivo + 1
    elif n < 0:
        negativo = negativo + 1
    else:
        nulo += 1
print(f"""
    Positivos: {positivo}
    Negativos: {negativo}
    Nulos: {nulo}
""")