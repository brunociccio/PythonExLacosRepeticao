"""
Em uma sala tem 5 alunos, cada um faz 2 provas.
A media para aprovar ou não é 5.
Contar quantos alunos foram aprovados e quantos foram reprovados.
"""
alunoAprovado = 0
alunoReprovado = 0
for volta in range(1, 5 + 1, 1):
    print(f"--- Aluno --- {volta}")
    n1 = float(input("Digite a sua primeira nota: "))
    n2 = float(input("Digite a sua segunda nota: "))
    med = (n1 + n2) / 2
    print(f"Média = {med}")
    if med > 5:
        alunoAprovado = alunoAprovado + 1
    else:
        alunoReprovado = alunoReprovado + 1
print(f"""
    Alunos Aprovados: {alunoAprovado}
    Alunos Reprovados: {alunoReprovado}
    """)

