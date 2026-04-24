# Validação de entrada, número positivo, com tratamento de erros

# Inicializamos a variável com 0 para garantir que o ciclo começa
numero = 0

# O ciclo continua enquanto o número for menor ou igual a 0
while numero <= 0:

    try:
        # Pedimos um número ao utilizador e convertemos diretamente para float
        numero = float(input("Introduz um número positivo: "))

        # Verificamos se o número é menor ou igual a 0
        if numero <= 0:
            print("Erro: o número deve ser positivo. Tenta novamente.")

    except ValueError:
        # Esta parte é executada se o utilizador escrever algo que não seja número
        print("Erro: introduz um valor numérico válido.")

# Quando chegamos aqui, significa que o número é válido e positivo
print(f"Obrigado! Introduziste o número positivo {numero}.")

