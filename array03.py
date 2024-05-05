# Lendo os números reais e armazenando em um vetor
print("Digite 10 números reais:")
numeros_reais = [
    float(input("Digite o 1º número: ")),
    float(input("Digite o 2º número: ")),
    float(input("Digite o 3º número: ")),
    float(input("Digite o 4º número: ")),
    float(input("Digite o 5º número: ")),
    float(input("Digite o 6º número: ")),
    float(input("Digite o 7º número: ")),
    float(input("Digite o 8º número: ")),
    float(input("Digite o 9º número: ")),
    float(input("Digite o 10º número: "))
]

# Calculando os quadrados dos números reais sem usar for
quadrados = [
    numeros_reais[0] ** 2,
    numeros_reais[1] ** 2,
    numeros_reais[2] ** 2,
    numeros_reais[3] ** 2,
    numeros_reais[4] ** 2,
    numeros_reais[5] ** 2,
    numeros_reais[6] ** 2,
    numeros_reais[7] ** 2,
    numeros_reais[8] ** 2,
    numeros_reais[9] ** 2
]

# Imprimindo os conjuntos
print("\nConjunto de números reais:")
print(numeros_reais)
print("\nConjunto de quadrados:")
print(quadrados)
