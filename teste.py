try:  # Try Except
    num = float(input("Digite um número: "))
    print(5/num)
except ValueError:
    print("Você não digitou um número")
    
except ZeroDivisionError:
    print("Divisão por zero")
print("Fim!")