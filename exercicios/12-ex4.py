# iteração for sobre uma lista de frutas


# Lista de frutas
frutas = ["maçã", "banana", "laranja", "uva"]

# com o ciclo for iterar a lista e mostrar cada fruta com o seu índice
for indice, fruta in enumerate(frutas, start=1):
    print(f"{indice}. {fruta}")

# Mostra o total de frutas na lista
print(f"Total de frutas: {len(frutas)}")

