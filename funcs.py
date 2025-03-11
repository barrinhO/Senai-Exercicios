#Exercícios de funções

#Exercício 1

def piramide(n):
    for i in range(n):
        print(str(i+1) * (i+1))

piramide(5)

#Exercício 2

def piramideCrescente(n):
    for i in range(n):
        for j in range(1,i+2):
            print(j, end=" ")
        print()
        
piramideCrescente(5)

    
#Exercicio 3

def sumArgs(x,y,z):
    print(f"Soma: {x + y + z}")
    
sumArgs(x=1, y=2, z=3)


# Exercicio 4

def caracteres(n):
    if n > 0:
        return "P"
    return "N"
    
caracteres(-1)
    
#Exercicio 5

def somaImposto(custo, taxaImposto):
    print(custo + (custo * taxaImposto/100))

somaImposto(200, 50)


#Exercicio 6

# Verificação

def verificarCpf():
    lista = []
    multiplicações = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    

