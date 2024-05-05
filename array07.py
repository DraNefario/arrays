# Lendo 10 números inteiros e armazenando em um vetor
print("Digite 10 números inteiros:")
vetor = [
    int(input("Digite o número 1: ")),
    int(input("Digite o número 2: ")),
    int(input("Digite o número 3: ")),
    int(input("Digite o número 4: ")),
    int(input("Digite o número 5: ")),
    int(input("Digite o número 6: ")),
    int(input("Digite o número 7: ")),
    int(input("Digite o número 8: ")),
    int(input("Digite o número 9: ")),
    int(input("Digite o número 10: "))
]

# Encontrando o maior elemento e sua posição
maior = max(vetor)
posicao_maior = vetor.index(maior)

# Imprimindo o vetor, o maior elemento e sua posição
print("Vetor:", vetor)
print("Maior elemento:", maior)
print("Posição do maior elemento:", posicao_maior)