

# exercicio 1 for
string = "abóbora"
print(f"Primeira string: {string}")
char = string.split(" ")
print("Segunda string: ")
for char in string:
    print(f"*{char}", end="")


#While 

texto1 = input("texto: ")
texto2 = "*"
indice = 0
while indice < len(texto1):
    texto2 += texto2[indice]+"*"
    indice += 1
print(texto2)
    
    
# exercício 2

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
soma = num1 + num2
sub =  num1 - num2
mult = num1 * num2
div = num1 / num2

print("Utilize 1 para somar")
print("Utilize 2 para subtrair")
print("Utilize 3 para multiplicar")
print("Utilize 4 para dividir")

operacao = str(input("Qual operação você deseja fazer? "))

if(operacao == '1'):
    print(f"Soma: {soma}")
elif(operacao == '2'):
    print(f"Subtração: {sub}")
elif(operacao == '3'):
    print(f"Multiplicação: {mult}")
elif(operacao == '4'):
    print(f"Divisão: {div}")
else:
    print("Por favor digite o numero da operação")
    
# # Exercicio 4

# frase = "Eu gosto de morango"
# for char in frase:
#   chars = print(char, "=", frase.count(char))
  
#   if(char == 4):
#       print("o")

  


    

    