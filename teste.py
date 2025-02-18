#Exercício 2 18-02-25


seu_nome = str(input("Digite seu nome: "))

if(len(seu_nome) <= 4):
    print("Seu nome é curto!")
    
elif(len(seu_nome) == 5 or len(seu_nome) == 6 ):
    print("Seu nome é normal!")
    
elif(len(seu_nome) ==    9):
    print("Seu nome é muito grande")
    
else:
    print("Seu nome é gigantee meu nobre!")