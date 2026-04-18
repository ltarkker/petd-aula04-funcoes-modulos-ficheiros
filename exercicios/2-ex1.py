# exemplo de estruturas condicionais
idade = int(input("Digite a sua idade: "))

# if-elif-else
if idade < 0:
    print("Idade inválida.")
elif idade < 18:
    print("Menor de idade.")
elif idade < 65:
    print("Adulto.")
else:
    print("Idoso.")
    
    