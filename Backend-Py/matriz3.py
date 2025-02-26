
#          0   1   2   3 COLUNAS
matriz = [[10, 8, 15, 12], # LINHA 0
          [21, 11, 23, 8], # LINHA 1
          [14, 5, 13, 19]] # LINHA 2

print(f"\n{matriz[0]}\n{matriz[1]}\n{matriz[2]}")



M = 3 # 3 LINHAS
N = 4 # 4 COLUNAS
# Matriz 3x4

X = int(input("Digite um número inteiro presente na matriz: ")) # Exemplo 23

for i in range(M): # 0, 1, 2 linhas
    for j in range(N): # 0, 1, 2, 3 colunas
        if matriz[i][j] == X: # Se o valor da matriz na posição i, j for igual a X
            print(f"Posição: {i}, {j}") # Mostra a posição de X, linha i, coluna j 
            
            if j > 0: # Se j for maior que 0, ou seja não for a primeira coluna
                print(f"Esquerda: {matriz[i][j-1]}") # Mostra o valor a esquerda de X, j-1 significa a coluna anterior, neste caso a esquerda
                
            if i > 0: # Se i for maior que 0 ou seja não for a primeira linha 
                print(f"Cima: {matriz[i-1][j]}") # Mostra o valor acima de X, i-1 significa a linha anterior, neste caso a de cima
                
            if j < N - 1: # Se j for menor que N - 1 ou seja não for a última coluna
                print(f"Direita: {matriz[i][j+1]}") # Mostra o valor a direita de X, j+1 significa a próxima coluna, neste caso a direita
                
            if i < M - 1: # Se i for menor que M - 1 ou seja não for a última linha
                print(f"Baixo: {matriz[i+1][j]}") # Mostra o valor abaixo de X, i+1 significa a próxima linha, neste caso a de baixo
                
    print() # Pula a linha

