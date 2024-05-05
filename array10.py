# Lendo 5 valores
print("Digite 5 valores:")
valores = [
    float(input("Digite o valor 1: ")),
    float(input("Digite o valor 2: ")),
    float(input("Digite o valor 3: ")),
    float(input("Digite o valor 4: ")),
    float(input("Digite o valor 5: "))
]

# Calculando o maior, o menor e a média dos valores
maior = max(valores)
menor = min(valores)
media = sum(valores) / len(valores)

# Mostrando todos os valores, o maior, o menor e a média
print("Valores lidos:", valores)
print("Maior valor:", maior)
print("Menor valor:", menor)
print("Média dos valores:", media)
