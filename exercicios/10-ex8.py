# Definição da função para verificar se um número é par
def e_par(numero):
    
    """
    Verifica se um número é par.
    Parâmetros:
    numero (int): O número a ser verificado
    Retorna:
    bool: True se o número for par, False se for ímpar
    """
    
    return numero % 2 == 0

# Teste da função
print(f"4 é par? {e_par(4)}")
print(f"7 é par? {e_par(7)}")
print(f"0 é par? {e_par(0)}")
print(f"-2 é par? {e_par(-2)}")


# Utilizando o valor retornado em uma estrutura condicional
numero = 15

if e_par(numero):
    print(f"{numero} é um número par.")
else:
    print(f"{numero} é um número ímpar.")



