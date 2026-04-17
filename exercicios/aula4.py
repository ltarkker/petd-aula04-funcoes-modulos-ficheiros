# calculadores básica

# entrada de dados
# pedir ao user o primeiro número
num1 = float(input("Digite o primeiro número: "))

# pedir ao utilizador o segundo número
num2 = float(input("Digite o segundo número: "))

# operações matemáticas
# 1 - soma
soma = num1 + num2
 
# 2 - subtração
subtracao = num1 - num2

# 3 - multiplicação
multiplicacao = num1 * num2

# Mostar os resultados
print("A soma é:", soma)
print("A subtração é:", subtracao)
print("A multiplicação é:", multiplicacao)

# verificar se o segundo número é diferente de zero para evitar divisão por zero
if num2 != 0:
    # calcular a divisão
    divisao = num1 / num2
    print("A divisão é:", divisao)
    
else:
    print("Não é possível dividir por zero.")
    
    
