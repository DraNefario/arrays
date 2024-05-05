# Lendo 5 valores
print("Digite 5 valores:")
valores = [
    float(input("Digite o valor 1: ")),
    float(input("Digite o valor 2: ")),
    float(input("Digite o valor 3: ")),
    float(input("Digite o valor 4: ")),
    float(input("Digite o valor 5: "))
]

# Encontrando a posição do maior e do menor valor
posicao_maior = valores.index(max(valores)) + 1
posicao_menor = valores.index(min(valores)) + 1

# Mostrando as posições do maior e do menor valor
print("Posição do maior valor:", posicao_maior)
print("Posição do menor valor:", posicao_menor)
