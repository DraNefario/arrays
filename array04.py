# Lendo um vetor de 8 posições
print("Digite 8 valores:")
vetor = [
    int(input("Digite o valor 1: ")),
    int(input("Digite o valor 2: ")),
    int(input("Digite o valor 3: ")),
    int(input("Digite o valor 4: ")),
    int(input("Digite o valor 5: ")),
    int(input("Digite o valor 6: ")),
    int(input("Digite o valor 7: ")),
    int(input("Digite o valor 8: "))
]

# Lendo os valores de X e Y
x = int(input("Digite o valor de X (entre 0 e 7): "))
y = int(input("Digite o valor de Y (entre 0 e 7): "))

# Verificando se os valores de X e Y estão dentro do intervalo válido
if x < 0 or x > 7 or y < 0 or y > 7:
    print("Posições inválidas.")
else:
    # Calculando a soma dos valores nas posições X e Y
    soma = vetor[x] + vetor[y]
    print("A soma dos valores nas posições {} e {} é: {}".format(x, y, soma))
