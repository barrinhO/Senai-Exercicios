matriz = [
    [5, -2],
    [3, 4]
]

for linha in enumerate(matriz):
    for coluna in enumerate(linha[1]):
        if linha[0] == coluna [0]:
            print(coluna[1])

qtdNegativo = 0
for linha in matriz:
    for coluna in linha:
        if coluna < 0:
            qtdNegativo += 1
print(f"Quantidade de negativos: {qtdNegativo}")