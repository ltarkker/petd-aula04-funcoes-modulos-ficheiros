# Ficheiro: main.py
# Diferentes formas de importação (requisito 5)
import utilidades                          # forma 1: módulo completo
from utilidades import e_par               # forma 2: função específica
from utilidades import calcular_media as media  # forma 3: com alias


def main():
    print("Demonstração do módulo de utilidades")
    print("-" * 40)

    # Forma 1: usar via nome do módulo
    a, b = 10, 5
    resultado = utilidades.somar(a, b)
    print(f"{a} + {b} = {resultado}")

    # Forma 2: usar função importada directamente
    for num in [1, 2, 3, 4, 5]:
        if e_par(num):
            print(f"{num} é par")
        else:
            print(f"{num} é ímpar")

    # Forma 3: usar com alias
    notas = [85, 90, 78, 92, 88]
    resultado_media = media(notas)
    print(f"A média das notas {notas} é {resultado_media:.1f}")


if __name__ == "__main__":
    main()


