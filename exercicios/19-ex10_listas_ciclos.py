# Lista de frutas
frutas = ["maçã", "banana", "laranja", "uva"]

# Percorrer a lista diretamente pelos elementos
for fruta in frutas:

    # Em cada repetição, a variável fruta recebe um elemento da lista
    print(f"Fruta: {fruta}")


# Percorrer a lista usando índices
# len(frutas) devolve o número de elementos da lista
# range(len(frutas)) gera os índices: 0, 1, 2, 3
for i in range(len(frutas)):

    # i representa o índice atual
    # frutas[i] permite aceder ao elemento nessa posição
    print(f"Índice {i}: {frutas[i]}")


