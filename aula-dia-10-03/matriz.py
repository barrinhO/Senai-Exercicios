import random

numero = int(input("Digite um número: "))
matriz = []
print("Matriz:")
for linha in range(numero):
    linhaLista = []
    for coluna in range(numero):
        linhaLista.append(random.randint(-10, 10))
    matriz.append(linhaLista)
    print()
    
print(matriz)
    
qtdNegativo = 0
for linha in matriz:
    for coluna in linha:
        if coluna < 0:
            qtdNegativo +=1
            
print(f"Quantidade de números negativos: {qtdNegativo}")

for linhaEnum in enumerate(matriz):
    for colunaEnum in enumerate(linhaEnum[1]):
        if(colunaEnum[0] == linhaEnum[0]):
            print(colunaEnum[1])