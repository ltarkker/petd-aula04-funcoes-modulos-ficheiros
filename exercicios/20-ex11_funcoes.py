# ===============================
# FUNÇÕES EM PYTHON
# ===============================

# Uma função é um bloco de código que podemos reutilizar.
# Para criar uma função usamos def.


# 1. Função simples, sem parâmetros
def mostrar_mensagem():
    print("Bem-vindo à aula de Python!")


# Chamar a função
mostrar_mensagem()


# 2. Função com parâmetro
def cumprimentar(nome):
    print(f"Olá, {nome}!")


cumprimentar("Ana")
cumprimentar("João")


# 3. Função com dois parâmetros
def somar(a, b):
    resultado = a + b
    print(f"A soma é: {resultado}")


somar(5, 3)


# 4. Função com return
def calcular_area_retangulo(base, altura):
    area = base * altura
    return area


resultado = calcular_area_retangulo(5, 3)
print(f"A área do retângulo é: {resultado}")


# 5. Função para verificar se um número é par
def e_par(numero):
    return numero % 2 == 0


numero = 8

if e_par(numero):
    print(f"{numero} é par.")
else:
    print(f"{numero} é ímpar.")

