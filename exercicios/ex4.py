# Classificação de número

# Entrada de dados
numero_str = input("Digite um número: ")

# Conversão para float
numero = float(numero_str)

# Verificação e classificação
if numero > 0:
    print(f"O número {numero} é positivo.")
elif numero < 0:
    print(f"O número {numero} é negativo.")
else:
    print("O número é zero.")
    
    
    