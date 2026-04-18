# Definição da função de soma
def somar(a, b):
    """
    Soma dois números e retorna o resultado.
    Parâmetros:
    a (float): Primeiro número
    b (float): Segundo número
    Retorna:
    float: A soma de a e b
    """
    resultado = a + b
    return resultado


# Teste da função
print(f"Soma de 5 e 3: {somar(5, 3)}")
print(f"Soma de -2 e 7: {somar(-2, 7)}")
print(f"Soma de 1.5 e 2.5: {somar(1.5, 2.5)}")

# Utilizando o valor retornado
total = somar(10, 20)
print(f"O total é {total}")
print(f"O dobro da soma é {total * 2}")

