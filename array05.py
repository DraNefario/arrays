# Lendo um vetor de 10 posições
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

# Contando os valores pares
pares = len(list(filter(lambda x: x % 2 == 0, vetor)))

# Escrevendo a quantidade de valores pares
print("O vetor possui", pares, "valores pares.")
