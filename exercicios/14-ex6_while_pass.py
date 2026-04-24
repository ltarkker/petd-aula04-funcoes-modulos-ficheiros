# Validação da password

# Definimos a password correcta
senha_correta = "12345"

# Criamos a varável vazia para guardar a tentativa do user
tentativa = ""

# Criamos um ciclo while que repete enquanto a tentativa for diferente da senha correcta
while tentativa != senha_correta:
    tentativa = input("Digite a password: ")

    # Se a tentativa estiver eerada, mostramos uma mensagem de erro
    if tentativa != senha_correta:
        print("Password incorreta. Tente novamente.")

# Quando o ciclo termina, significa que a password está correcta
print("Password correta! Acesso permitido.")

