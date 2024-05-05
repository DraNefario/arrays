# Lendo a nota da prova de 15 alunos e armazenando num vetor
print("Digite as notas das provas dos 15 alunos:")
notas = [
    float(input("Nota do aluno 1: ")),
    float(input("Nota do aluno 2: ")),
    float(input("Nota do aluno 3: ")),
    float(input("Nota do aluno 4: ")),
    float(input("Nota do aluno 5: ")),
    float(input("Nota do aluno 6: ")),
    float(input("Nota do aluno 7: ")),
    float(input("Nota do aluno 8: ")),
    float(input("Nota do aluno 9: ")),
    float(input("Nota do aluno 10: ")),
    float(input("Nota do aluno 11: ")),
    float(input("Nota do aluno 12: ")),
    float(input("Nota do aluno 13: ")),
    float(input("Nota do aluno 14: ")),
    float(input("Nota do aluno 15: "))
]

# Calculando a média geral
media_geral = sum(notas) / len(notas)

# Imprimindo a média geral
print("Média geral:", media_geral)