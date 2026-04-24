# 🐍 [PETD] Aula 04 — Funções Avançadas, Módulos e Ficheiros

> Programação Estruturada e Tipos de Dados · CTeSP em Redes e Sistemas Informáticos · ISTEC Porto · 2025/2026

---

## 📋 Informações da UC

| Campo | Detalhe |
|---|---|
| **Unidade Curricular** | Programação Estruturada e Tipos de Dados (PETD) |
| **Docente** | Mário Amorim |
| **Curso** | CTeSP em Redes e Sistemas Informáticos |
| **Período** | 2.º Semestre |
| **Ano** | 1.º Ano |
| **Ano Letivo** | 2025/2026 |
| **Aluno** | Gonçalo Lopes Fernandes (N.º 2022148) |
| **Nota Final** | A aguardar (publicação prevista em julho 2026) |

---

## 📁 Estrutura do Repositório

```
petd-aula04-funcoes-modulos-ficheiros/
├── exercicios/                    # Exercícios realizados em aula
│   ├── meu_projeto/               # Projecto modular (módulos + imports)
│   │   ├── main.py                # Ponto de entrada com 3 formas de import
│   │   └── utilidades.py          # Módulo com funções reutilizáveis
│   ├── 1-ex.py
│   ├── 2-ex1.py
│   ├── ...
│   └── 20-ex11_funcoes.py
├── docs/                          # Pseudocódigo e fluxogramas
│   └── apps-logic.txt             # 5 fluxogramas de aplicações
├── notas/                         # Apontamentos e notas pessoais
├── .gitignore
├── commands.txt                   # Atalhos de navegação PowerShell
└── README.md
```

---

## 📝 Trabalhos Realizados

### Exercícios

| # | Ficheiro | Conceito |
|---|---|---|
| 1 | `1-ex.py` | Calculadora básica com `input`/`print` e divisão segura |
| 2 | `2-ex1.py` | Condicionais encadeadas (`if`/`elif`/`else`) aplicadas a idade |
| 3 | `3-ex2.py` | Comparação de dois números com conversão explícita |
| 4 | `4-ex3.py` | Classificação de número (positivo, negativo, zero) |
| 5 | `5-ex4.py` | Cálculo de média com ciclo `for` e acumulador |
| 6 | `6-ciclos.py` | Contagem regressiva com `while` |
| 7 | `7-ex5.py` | Validação de número positivo com `while` |
| 8 | `8-ex6.py` | Listas: iteração directa e com índices |
| 9 | `9-ex7.py` | Função `somar()` com `return` e docstring |
| 10 | `10-ex8.py` | Função `e_par()` aplicada ao operador módulo |
| 11 | `11-ex3.py` | Comparação de números (versão compacta) |
| 12 | `12-ex4.py` | Iteração sobre lista com `enumerate()` |
| 13 | `13-ex5_while.py` | Contagem regressiva com `while` decrementado |
| 14 | `14-ex6_while_pass.py` | Validação de password com ciclo `while` |
| 15 | `15-ex7_media.py` | Média de 5 números com acumulador e formatação |
| 16 | `16-ex8_positivo_while.py` | Validação de número positivo (sem `try`) |
| 17 | `17-ex9_listas.py` | Métodos de listas (`append`, `insert`, `remove`, `pop`) |
| 18 | `18-while-tryexcept.py` | Validação robusta com `try`/`except ValueError` |
| 19 | `19-ex10_listas_ciclos.py` | Percorrer listas com `for` directo e por índices |
| 20 | `20-ex11_funcoes.py` | Funções: sem parâmetros, com parâmetros e com `return` |

### Projecto modular — `exercicios/meu_projeto/`

Demonstra as **três formas de importação** em Python:

```python
import utilidades                                # módulo completo
from utilidades import e_par                     # função específica
from utilidades import calcular_media as media   # com alias
```

O módulo `utilidades.py` expõe:

- `somar(a, b)` — soma dois números
- `e_par(numero)` — verifica paridade
- `calcular_media(numeros)` — média de uma lista (com validação de lista vazia)

Execução:

```powershell
cd exercicios\meu_projeto
python main.py
```

### Pseudocódigo — `docs/apps-logic.txt`

Cinco fluxogramas em texto que descrevem o algoritmo de aplicações-tipo:

1. **Gerador de passwords** — composição de pool e selecção aleatória
2. **Calculadora de estatísticas** — média, mediana, mínimo, máximo
3. **Processamento de texto** — linhas, palavras, caracteres, palavra mais longa
4. **Contagem de linhas em ficheiro** — total, branco, comentário, código
5. **Análise de CSV** — cabeçalhos, registos, dados

Incluem-se ainda padrões recorrentes: validação inicial com *early return*, uso de `with open()`, retorno de múltiplos valores em dicionário, *list comprehensions* e aproveitamento de *built-ins*.

---

## 🧠 Temas Abordados

| Tema | Conteúdo | Estado |
|---|---|---|
| Entrada/saída | `input()`, `print()`, f-strings, conversão de tipos | ✅ |
| Condicionais | `if`, `elif`, `else`, operadores de comparação | ✅ |
| Ciclo `for` | `range()`, iteração directa, `enumerate()` | ✅ |
| Ciclo `while` | Condições, acumuladores, contadores | ✅ |
| Listas | `append`, `insert`, `remove`, `pop`, iteração | ✅ |
| Funções | `def`, parâmetros, `return`, docstrings | ✅ |
| Módulos e imports | `import`, `from ... import`, alias com `as` | ✅ |
| Tratamento de erros | `try`/`except` com `ValueError` | ✅ |
| Ficheiros de texto | `with open()`, `read()`, `readlines()`, `write()` | 🔜 |

---

## 📬 Contacto

**Gonçalo Lopes Fernandes**
📧 goncalo.fernandes.2022148@my.istec.pt

---

*Repositório académico criado no âmbito do CTeSP em Redes e Sistemas Informáticos — ISTEC Porto, 2025/2026.*
