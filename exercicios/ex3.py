# Comparação de números

# Entrada de dados
num1_str = input("Digite o primeiro número: ")
num2_str = input("Digite o segundo número: ")

# Conversão para float
num1 = float(num1_str)
num2 = float(num2_str)

# Comparação e saída
if num1 > num2:
    print(f"O primeiro número {num1} é maior que o segundo {num2}.")
elif num2 > num1:
    print(f"O segundo número {num2} é maior que o primeiro {num1}.")
else:
    print(f"Os números são iguais ({num1}).")
    
    