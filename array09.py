# Preenchendo um vetor com 10 números reais
print("Digite 10 números reais:")
numeros = [
    float(input("Digite o número 1: ")),
    float(input("Digite o número 2: ")),
    float(input("Digite o número 3: ")),
    float(input("Digite o número 4: ")),
    float(input("Digite o número 5: ")),
    float(input("Digite o número 6: ")),
    float(input("Digite o número 7: ")),
    float(input("Digite o número 8: ")),
    float(input("Digite o número 9: ")),
    float(input("Digite o número 10: "))
]

# Calculando a quantidade de números negativos e a soma dos positivos
negativos = len(list(filter(lambda x: x < 0, numeros)))
soma_positivos = sum(filter(lambda x: x > 0, numeros))

# Mostrando os resultados
print("Quantidade de números negativos:", negativos)
print("Soma dos números positivos:", soma_positivos)
