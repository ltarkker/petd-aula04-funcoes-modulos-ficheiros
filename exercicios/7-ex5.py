# Validação de entrada - número positivo
# Inicialização da variável
numero = 0

# Ciclo while para validação
while numero <= 0:
    numero_str = input("Digite um número positivo: ")
    numero = float(numero_str)
    
if numero <= 0:
    print("Erro: O número deve ser positivo.")
    print("Tente novamente.")

    # Mensagem final
    print(f"Obrigado! Você digitou o número positivo {numero}.")
    
    