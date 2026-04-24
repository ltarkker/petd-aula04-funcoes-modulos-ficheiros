# Validação de entrada, número positivo

# Inicializamos a variável com 0
# Assim garantimos que o ciclo while começa, porque 0 não é positivo
numero = 0

# O ciclo repete enquanto o número for menor ou igual a 0
while numero <= 0:

    # Pedimos ao utilizador para introduzir um número
    numero_str = input("Introduz um número positivo: ")

    # Convertemos o valor introduzido para float
    # Usamos float para aceitar números inteiros e decimais
    numero = float(numero_str)

    # Se o número não for positivo, mostramos uma mensagem de erro
    if numero <= 0:
        print("Erro: o número deve ser positivo. Tenta novamente.")

# Quando o ciclo termina, significa que o número é positivo
print(f"Obrigado! Introduziste o número positivo {numero}.")

