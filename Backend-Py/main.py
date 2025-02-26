# exercícios if e else

# ex 1
number1 = number1 = float(input("Digite um número: "))
number2 = number2 = float(input("Digite um número: "))
if(number1 > number2):
    print("O primeiro número é maior que o segundo")
else:
    print("O segundo número é maior que o primeiro")

# ex 2
num1 = float(input("Digite um número: "))
num2 = float(input("Digite um número: "))
if(num1 > 0):
    print("O primeiro número é positivo!")
elif(num1 < 0):
    print("O Primeiro número é negativo")
else:
    print("Digite um número")
if(num2 > 0):
    print("O segundo número é positivo!")
elif(num2 < 0):
    print("O segundo número é negativo")
else:
    print("Digite um número")


# ex 3
mas_ou_fem = str(input("Digite 'm' ou 'f' ")).lower()

if(mas_ou_fem == 'm' or "M"):
    print("Homem")
elif(mas_ou_fem == 'f'):
    print("Mulher")
else:
    print("Por favor digite 'm' ou 'y' ")
    
    
# ex 4
name_user = str(input("Por favor digite seu nome: "))
age_user = input("Por favor digite sua idade: ")

if name_user and age_user:
    age_user = int(age_user)
    print(f"Seu nome é: {name_user}.")
    print(f"Seu nome invertido é: {name_user[::-1]}")
    print(f"Seu nome tem '{len(name_user)}' letras")
    print(f"A primeira letra do seu nome é: {name_user[0]}")
    print(f"A última letra do seu nome é: {name_user[-1]}")
    if(name_user == " "):
        print("Seu nome contém espaços!")
    else:
        print("Seu nome não contém espaços!")
    
else:
    print("Por favor digite seu nome e sua idade")
    
    
# ex 5

# ex 4

string1 = "cleitinho"
string2 = "dilsorobis"
tamanho_string1 = len(string1)
tamanho_string2 = len(string2)

print(f"A primeira string é: {string1}.")
print(f"A segunda string é {string2}.")

if tamanho_string1 == tamanho_string2:
    print("As duas strings possuem o mesmo comprimento.")
else:
    print("Os comprimentos das strings são diferentes.")
    
if string1 == string2:
    print("Os conteúdos strings são iguais")
else:
    print("Os conteúdos das strings são diferentes")


# ex 6

name_user = str(input("Digite seu nome: "))
print(f"Seu nome: {name_user}")
print(f"Seu nome de trás para frente: {name_user[::-1].upper()}")

# ex 7

user_string = str(input("Digite uma frase: "))
user_string_spaces = user_string.count(" ")
vogais = ['a', 'e', 'i', 'o', 'u']

if user_string:
    print(f"Sua frase: {user_string}")
    print(f"Espaços em branco na sua frase: {user_string_spaces}")

if(user_string_spaces == 0):
    print("não há espaços na frase")
    
vogais_presentes = [vogal for vogal in vogais if vogal in user_string]

if(vogais_presentes):
    print(f"As vogais {vogais_presentes} estão presentes na string.")
else:
    print("Nenhum das vogais está presente na string.")
        
# ex 8
letra = input("Digite uma letra: ")
vogais = ['a', 'e', 'i', 'o', 'u']

if(letra in vogais):
    print("Esta letra é uma vogal.")
else:
    print("Esta letra é uma consoante.")
    
# ex 9

media1 = float(input("Digite sua primeira média: "))
media2 = float(input("Digite sua segunda média: "))
media3 = float(input("Digite sua terceira média: "))

soma_medias = (media1 + media2 + media3) / 3

if(soma_medias >= 7):
    print("Aprovado!")
elif(soma_medias < 7):
    print("Reprovado")
elif(soma_medias == 10):
    print("Aprovado por Distinção")
    
print(f"Sua média: {soma_medias}")


# ex 10

num1 = float(input("Digite um número: "))
num2 = float(input("Digite um número: "))
num3 = float(input("Digite um número: "))

print(f"Primeiro número: {num1}")
print(f"Segundo número: {num2}")
print(f"Terceiro número: {num3}")


if(num1 > num2 and num3):
    print("O primeiro número é o maior.")
elif(num2 > num1 and num3):
    print("O segundo número é o maior")
elif(num3 > num1 and num3):
    print("O terceiro número é o maior")
else:
    print("Todos números são iguais")


# 11

num1 = float(input("Digite um número: "))
num2 = float(input("Digite um número: "))
num3 = float(input("Digite um número: "))

print(f"Primeiro número: {num1}")
print(f"Segundo número: {num2}")
print(f"Terceiro número: {num3}")


if(num1 > num2 and num3):
    print(f"O primeiro número é maior que {num2} e {num3}")
elif(num2 > num1 and num3):
    print(f"O segundo número é maior que {num1} e {num3}")
elif(num3 > num1 and num2):
    print(f"O terceiro número é maior que {num1} e {num2}")
elif(num1 < num2 and num3):
    print(f"O primeiro número é menor que {num2} e {num3}")
elif(num2 < num1 and num3):
    print(f"O segundo número é menor que {num1} e {num3}")
elif(num3 < num1 and num2):
    print(f"O terceiro número é menor que {num1} e {num2}")
else:
    print(f"Todos números são iguais")
    
    
# ex 12

produto1 = input("Qual o preço do produto 1: ")
produto2 = input("Qual o preço do produto 2: ")
produto3 = input("Qual o preço do produto 3: ")

produto_acessível = min(produto1, produto2, produto3)

if(produto1 in produto_acessível):
    print("Compre o primeiro produto!")
elif(produto2 in produto_acessível):
    print("Compre o segundo produto!")
elif(produto3 in produto_acessível):
    print("Compre o produto 3!")
else:
    print("Num compensa")

# ex 13
numsDec = [int(input("Num1: ")), int(input("Num2: ")), int(input("Num3: "))]
numsCre = numsDec.sort(reverse = False)
print(f"Ordem decrescente: {numsDec.sort(reverse = True)}")
print(f"Ordem crescente: {numsCre}")

# ex 14
print("Digite 'm' para manhã, 'v' para tarde e 'n' para noturno.")
turno = str(input("Em que turno você estuda: ")).lower()

if(turno == 'm'):
    print("Bom dia")
elif(turno == 'v'):
    print("Boa tarde")
elif(turno == 'n'):
    print("Boa noite")
else:
    print("Você não estuda vagabundo, não sabe ler??")
    print("'m' 'v'ou 'n' ")
    
# ex 12

