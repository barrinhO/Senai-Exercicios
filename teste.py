#Exercício 1 18-02-25
try:
    int_num = int(input("Digite um número inteiro: "))
    resto = int_num % 2
    if(resto == 0):
        print("Número par")
    else:
        print("ímpar")
except:
    print("Por favor digite um número inteiro: ")
