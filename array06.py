# Recebendo do usuário um vetor com 10 posições
print("Digite 10 valores:")
vetor = [
    int(input("Digite o valor 1: ")),
    int(input("Digite o valor 2: ")),
    int(input("Digite o valor 3: ")),
    int(input("Digite o valor 4: ")),
    int(input("Digite o valor 5: ")),
    int(input("Digite o valor 6: ")),
    int(input("Digite o valor 7: ")),
    int(input("Digite o valor 8: ")),
    int(input("Digite o valor 9: ")),
    int(input("Digite o valor 10: "))
]

# Encontrando o maior e o menor elemento do vetor
maior = max(vetor)
menor = min(vetor)

# Imprimindo o maior e o menor elemento
print("Maior elemento:", maior)
print("Menor elemento:", menor)