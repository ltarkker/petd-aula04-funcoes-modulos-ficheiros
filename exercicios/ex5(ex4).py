# Cálculo de média de 5 números
# Inicialização da variável para acumular a soma

soma = 0

# Ciclo para ler 5 números
for i in range(5):
    numero_str = input(f"Digite o {i+1}o número: ")
    
numero = float(numero_str)
soma += numero
print(f"Soma atual: {soma}")

# Cálculo da média
media = soma / 5

# Apresentação do resultado
print(f"A média dos 5 números é: {media:.2f}")

