# Lista de nomes dos colegas
# Criação da lista

colegas = ["Ana", "Bruno", "Carlos",
"Diana", "Eduardo"]

# Percorrer a lista e imprimir cada nome
print("Lista de colegas:")
for nome in colegas:
    print(nome)
# Percorrer a lista com índices
    print("\nLista numerada de colegas:")
    
for i in range(len(colegas)):
    print(f"{i+1}. {colegas[i]}")
    
    