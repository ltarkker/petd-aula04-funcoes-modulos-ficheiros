# Cálculo da média de 5 números

# Variável para acumular a soma dos números introduzidos
soma = 0

# Quantidade de números que queremos pedir ao utilizador
quantidade = 5

# Ciclo para ler 5 números
for i in range(quantidade):

    # Pedir um número ao utilizador
    # O i começa em 0, por isso usamos i + 1 para mostrar 1.º, 2.º, 3.º, etc.
    numero_str = input(f"Digite o {i + 1}º número: ")

    # Converter o valor introduzido para float
    # Usamos float para permitir números inteiros e decimais
    numero = float(numero_str)

    # Adicionar o número à soma total
    soma += numero

    # Mostrar a soma acumulada até ao momento
    print(f"Soma atual: {soma}")

# Calcular a média
media = soma / quantidade

# Apresentar o resultado final com 2 casas decimais
print(f"A média dos {quantidade} números é: {media:.2f}")	


