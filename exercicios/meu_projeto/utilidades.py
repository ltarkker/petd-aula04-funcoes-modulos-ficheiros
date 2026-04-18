# Ficheiro: utilidades.py
def somar(a, b):
    """
    Soma dois números e retorna o resultado.
    Parâmetros:
        a (float): Primeiro número
        b (float): Segundo número
    Retorna:
        float: A soma de a e b
    """
    return a + b


def e_par(numero):
    """
    Verifica se um número é par.
    Parâmetros:
        numero (int): O número a ser verificado
    Retorna:
        bool: True se o número for par, False se for ímpar
    """
    return numero % 2 == 0


def calcular_media(numeros):
    """
    Calcula a média de uma lista de números.
    Parâmetros:
        numeros (list): Lista de números
    Retorna:
        float: A média dos números ou 0 se a lista estiver vazia
    """
    if not numeros:
        return 0
    return sum(numeros) / len(numeros)


