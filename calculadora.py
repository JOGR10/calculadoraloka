# CALCULADORA DE SISTEMAS DIGITAIS


from itertools import product
import re

# ============================================================

def separador():
    print("\n" + "=" * 70)


def binario_para_inteiro(valor):
    return int(valor, 2)


def validar_binario(valor):
    return all(c in "01" for c in valor)


def validar_hexadecimal(valor):
    try:
        int(valor, 16)
        return True
    except ValueError:
        return False


# ============================================================

def conversao_bases():
    separador()
    print("CONVERSÃO DE BASES")
    print("=" * 70)

    print("""
1 - Decimal
2 - Binário
3 - Octal
4 - Hexadecimal
""")

    origem = input("Escolha a base de origem: ").strip()

    bases = {
        "1": 10,
        "2": 2,
        "3": 8,
        "4": 16
    }

    if origem not in bases:
        print("Base inválida.")
        return

    valor = input("Digite o número: ").strip()

    try:
        decimal = int(valor, bases[origem])

        print("\nResultado:")
        print(f"Decimal:     {decimal}")
        print(f"Binário:     {bin(decimal)[2:]}")
        print(f"Octal:       {oct(decimal)[2:]}")
        print(f"Hexadecimal: {hex(decimal)[2:].upper()}")

    except ValueError:
        print("Número inválido para a base escolhida.")


# ============================================================

def decimal_para_bcd(numero):
    resultado = ""

    for digito in str(numero):
        resultado += format(int(digito), "04b") + " "

    return resultado.strip()


def decimal_para_gray(numero):
    binario = format(numero, "b")
    gray = binario[0]

    for i in range(1, len(binario)):
        gray += str(int(binario[i - 1]) ^ int(binario[i]))

    return gray


def decimal_para_excesso3(numero):
    resultado = ""

    for digito in str(numero):
        valor = int(digito) + 3
        resultado += format(valor, "04b") + " "

    return resultado.strip()


def tabela_ascii(caractere):
    codigo = ord(caractere)
    print(f"Caractere: {caractere}")
    print(f"Decimal:   {codigo}")
    print(f"Hexadecimal: {hex(codigo)[2:].upper()}")
    print(f"Binário:   {format(codigo, '08b')}")


def codigo_ebcdic(caractere):
    """
    Conversão básica usando tabela EBCDIC CP037.
    """

    tabela = {
        "A": "11000001",
        "B": "11000010",
        "C": "11000011",
        "D": "11000100",
        "E": "11000101",
        "F": "11000110",
        "G": "11000111",
        "H": "11001000",
        "I": "11001001",

        "J": "11010001",
        "K": "11010010",
        "L": "11010011",
        "M": "11010100",
        "N": "11010101",
        "O": "11010110",
        "P": "11010111",
        "Q": "11011000",
        "R": "11011001",

        "S": "11100010",
        "T": "11100011",
        "U": "11100100",
        "V": "11100101",
        "W": "11100110",
        "X": "11100111",
        "Y": "11101000",
        "Z": "11101001",

        "0": "11110000",
        "1": "11110001",
        "2": "11110010",
        "3": "11110011",
        "4": "11110100",
        "5": "11110101",
        "6": "11110110",
        "7": "11110111",
        "8": "11111000",
        "9": "11111001"
    }

    caractere = caractere.upper()

    if caractere in tabela:
        print(f"EBCDIC: {tabela[caractere]}")
    else:
        print("Caractere não disponível na tabela básica.")


def menu_codigos():
    separador()
    print("CÓDIGOS DIGITAIS")
    print("=" * 70)

    print("""
1 - BCD
2 - Gray
3 - EBCDIC
4 - ASCII
5 - Excesso-3
""")

    opcao = input("Escolha: ").strip()

    if opcao == "1":
        numero = input("Digite um número decimal: ")

        if numero.isdigit():
            print("BCD:", decimal_para_bcd(numero))
        else:
            print("Número inválido.")

    elif opcao == "2":
        numero = int(input("Digite um número decimal: "))

        if numero >= 0:
            print("Binário:", format(numero, "b"))
            print("Gray:   ", decimal_para_gray(numero))
        else:
            print("Digite um número positivo.")

    elif opcao == "3":
        caractere = input("Digite um caractere: ")

        if len(caractere) == 1:
            codigo_ebcdic(caractere)
        else:
            print("Digite apenas um caractere.")

    elif opcao == "4":
        caractere = input("Digite um caractere: ")

        if len(caractere) == 1:
            tabela_ascii(caractere)
        else:
            print("Digite apenas um caractere.")

    elif opcao == "5":
        numero = input("Digite um número decimal: ")

        if numero.isdigit():
            print("Excesso-3:", decimal_para_excesso3(numero))
        else:
            print("Número inválido.")

    else:
        print("Opção inválida.")


# ============================================================
# 3. OPERAÇÕES COM BASES NUMÉRICAS
# ============================================================

def operacoes_bases():
    separador()
    print("OPERAÇÕES COM BASES NUMÉRICAS")
    print("=" * 70)

    print("""
1 - Decimal
2 - Binário
3 - Octal
4 - Hexadecimal
""")

    base = input("Escolha a base: ").strip()

    bases = {
        "1": 10,
        "2": 2,
        "3": 8,
        "4": 16
    }

    if base not in bases:
        print("Base inválida.")
        return

    numero1 = input("Primeiro número: ").strip()
    operador = input("Operação (+, -, *, /): ").strip()
    numero2 = input("Segundo número: ").strip()

    try:
        n1 = int(numero1, bases[base])
        n2 = int(numero2, bases[base])

        if operador == "+":
            resultado = n1 + n2
        elif operador == "-":
            resultado = n1 - n2
        elif operador == "*":
            resultado = n1 * n2
        elif operador == "/":
            if n2 == 0:
                print("Não é possível dividir por zero.")
                return
            resultado = n1 // n2
        else:
            print("Operação inválida.")
            return

        print("\nResultado:")

        if resultado >= 0:
            print(f"Decimal:     {resultado}")
            print(f"Binário:     {bin(resultado)[2:]}")
            print(f"Octal:       {oct(resultado)[2:]}")
            print(f"Hexadecimal: {hex(resultado)[2:].upper()}")
        else:
            print(f"Decimal: {resultado}")

    except ValueError:
        print("Número inválido para a base selecionada.")


# ============================================================  

def AND(a, b):
    return a & b


def OR(a, b):
    return a | b


def NOT(a):
    return 1 - a


def NAND(a, b):
    return NOT(AND(a, b))


def NOR(a, b):
    return NOT(OR(a, b))


def XOR(a, b):
    return a ^ b


def XNOR(a, b):
    return NOT(XOR(a, b))


def portas_logicas():
    separador()
    print("PORTAS LÓGICAS")
    print("=" * 70)

    print("""
1 - AND
2 - OR
3 - NOT
4 - NAND
5 - NOR
6 - XOR
7 - XNOR
""")

    opcao = input("Escolha a porta: ")

    if opcao == "3":
        a = int(input("A (0 ou 1): "))

        if a not in [0, 1]:
            print("Valor inválido.")
            return

        print("NOT A =", NOT(a))
        return

    a = int(input("A (0 ou 1): "))
    b = int(input("B (0 ou 1): "))

    if a not in [0, 1] or b not in [0, 1]:
        print("Digite somente 0 ou 1.")
        return

    if opcao == "1":
        resultado = AND(a, b)
        nome = "AND"

    elif opcao == "2":
        resultado = OR(a, b)
        nome = "OR"

    elif opcao == "4":
        resultado = NAND(a, b)
        nome = "NAND"

    elif opcao == "5":
        resultado = NOR(a, b)
        nome = "NOR"

    elif opcao == "6":
        resultado = XOR(a, b)
        nome = "XOR"

    elif opcao == "7":
        resultado = XNOR(a, b)
        nome = "XNOR"

    else:
        print("Opção inválida.")
        return

    print(f"{nome}({a}, {b}) = {resultado}")


# ============================================================
# 5. TABELA VERDADE
# ============================================================

def avaliar_expressao(expressao, valores):
    """
    Avalia expressões usando:

    AND -> *
    OR  -> +
    NOT -> !

    Também aceita:
    A AND B
    A OR B
    NOT A
    """

    expressao = expressao.upper()

    expressao = expressao.replace("AND", "*")
    expressao = expressao.replace("OR", "+")
    expressao = expressao.replace("NOT", "!")

    # Substituição das variáveis
    for variavel, valor in sorted(valores.items(), key=lambda x: -len(x[0])):
        expressao = re.sub(
            r'\b' + re.escape(variavel) + r'\b',
            str(valor),
            expressao
        )

    # NOT
    while "!" in expressao:
        pos = expressao.rfind("!")

        i = pos + 1

        while i < len(expressao) and expressao[i] == " ":
            i += 1

        if i < len(expressao):
            valor = expressao[i]

            if valor == "0":
                novo = "1"
            else:
                novo = "0"

            expressao = expressao[:pos] + novo + expressao[i + 1:]

    # AND
    while "*" in expressao:
        expressao = re.sub(
            r'(\d)\s*\*\s*(\d)',
            lambda m: str(int(m.group(1)) & int(m.group(2))),
            expressao
        )

    # OR
    while "+" in expressao:
        expressao = re.sub(
            r'(\d)\s*\+\s*(\d)',
            lambda m: str(int(m.group(1)) | int(m.group(2))),
            expressao
        )

    return int(expressao.strip())


def tabela_verdade():
    separador()
    print("TABELA VERDADE")
    print("=" * 70)

    print("""
Utilize:
AND = *
OR  = +
NOT = !

Exemplo:
(A * B) + !C
""")

    expressao = input("Expressão booleana: ").strip()

    variaveis = sorted(set(re.findall(r'\b[A-Z]\b', expressao.upper())))

    if not variaveis:
        print("Nenhuma variável encontrada.")
        return

    print("\nTabela Verdade")
    print("-" * 70)

    print(" | ".join(variaveis) + " | S")
    print("-" * 70)

    for combinacao in product([0, 1], repeat=len(variaveis)):

        valores = dict(zip(variaveis, combinacao))

        try:
            resultado = avaliar_expressao(expressao, valores)
        except Exception:
            print("Erro ao interpretar a expressão.")
            return

        linha = " | ".join(str(v) for v in combinacao)

        print(f"{linha} | {resultado}")

# ============================================================

def algebra_booleana():
    separador()
    print("ÁLGEBRA BOOLEANA")
    print("=" * 70)

    print("""
Leis principais:

Identidade:
A + 0 = A
A * 1 = A

Dominação:
A + 1 = 1
A * 0 = 0

Idempotência:
A + A = A
A * A = A

Complementação:
A + !A = 1
A * !A = 0

Dupla negação:
!!A = A

Comutativa:
A + B = B + A
A * B = B * A

Associativa:
(A + B) + C = A + (B + C)
(A * B) * C = A * (B * C)

Distributiva:
A * (B + C) = AB + AC
A + BC = (A + B)(A + C)
""")

    expressao = input(
        "\nDigite uma expressão para aplicar algumas simplificações: "
    ).strip().upper()

    simplificada = simplificar_expressao(expressao)

    print("\nExpressão original:")
    print(expressao)

    print("\nExpressão simplificada:")
    print(simplificada)
# ============================================================

def simplificar_expressao(expressao):

    expressao = expressao.replace(" ", "")
    expressao = expressao.replace("AND", "*")
    expressao = expressao.replace("OR", "+")
    expressao = expressao.replace("NOT", "!")

    alterou = True

    while alterou:
        anterior = expressao

        # A + 0 = A
        expressao = re.sub(r'([A-Z])\+0', r'\1', expressao)
        expressao = re.sub(r'0\+([A-Z])', r'\1', expressao)

        # A * 1 = A
        expressao = re.sub(r'([A-Z])\*1', r'\1', expressao)
        expressao = re.sub(r'1\*([A-Z])', r'\1', expressao)

        # A * 0 = 0
        expressao = re.sub(r'([A-Z])\*0', '0', expressao)
        expressao = re.sub(r'0\*([A-Z])', '0', expressao)

        # A + 1 = 1
        expressao = re.sub(r'([A-Z])\+1', '1', expressao)
        expressao = re.sub(r'1\+([A-Z])', '1', expressao)

        # A + A = A
        expressao = re.sub(r'([A-Z])\+\1', r'\1', expressao)

        # A * A = A
        expressao = re.sub(r'([A-Z])\*\1', r'\1', expressao)

        # A + !A = 1
        expressao = re.sub(
            r'([A-Z])\+!\1',
            '1',
            expressao
        )

        # A * !A = 0
        expressao = re.sub(
            r'([A-Z])\*!\1',
            '0',
            expressao
        )

        if anterior == expressao:
            alterou = False

    return expressao

def karnaugh():
    separador()
    print("MAPA DE KARNAUGH")
    print("=" * 70)

    print("""
1 - 2 variáveis
2 - 3 variáveis
3 - 4 variáveis
""")

    opcao = input("Escolha: ")

    if opcao == "1":
        mapa_2_variaveis()

    elif opcao == "2":
        mapa_3_variaveis()

    elif opcao == "3":
        mapa_4_variaveis()

    else:
        print("Opção inválida.")


def mapa_2_variaveis():

    print("\nMAPA DE KARNAUGH - 2 VARIÁVEIS")

    print("""
        B
        0  1
A 0 |  |  |
  1 |  |  |
""")

    entrada = input(
        "Digite os 4 valores de saída na ordem 00,01,10,11: "
    )

    valores = entrada.split()

    if len(valores) != 4:
        print("Digite exatamente 4 valores.")
        return

    print("\n       B")
    print("       0  1")
    print(f"A=0 | {valores[0]}  {valores[1]}")
    print(f"A=1 | {valores[2]}  {valores[3]}")


def mapa_3_variaveis():

    print("\nMAPA DE KARNAUGH - 3 VARIÁVEIS")

    print("""
Digite os 8 valores:

ABC:
000
001
010
011
100
101
110
111
""")

    entrada = input("Valores separados por espaço: ")
    valores = entrada.split()

    if len(valores) != 8:
        print("Digite exatamente 8 valores.")
        return

    print("\n       BC")
    print("       00  01  11  10")
    print(f"A=0 |  {valores[0]}   {valores[1]}   {valores[3]}   {valores[2]}")
    print(f"A=1 |  {valores[4]}   {valores[5]}   {valores[7]}   {valores[6]}")


def mapa_4_variaveis():

    print("\nMAPA DE KARNAUGH - 4 VARIÁVEIS")

    print("""
Ordem Gray:

00  01  11  10

Digite os 16 valores.
""")

    entrada = input("Valores separados por espaço: ")
    valores = entrada.split()

    if len(valores) != 16:
        print("Digite exatamente 16 valores.")
        return

    print("\n             CD")
    print("             00  01  11  10")

    print(
        f"AB=00     | {valores[0]:>2}  {valores[1]:>2}  "
        f"{valores[3]:>2}  {valores[2]:>2}"
    )

    print(
        f"AB=01     | {valores[4]:>2}  {valores[5]:>2}  "
        f"{valores[7]:>2}  {valores[6]:>2}"
    )

    print(
        f"AB=11     | {valores[12]:>2} {valores[13]:>2} "
        f"{valores[15]:>2} {valores[14]:>2}"
    )

    print(
        f"AB=10     | {valores[8]:>2}  {valores[9]:>2}  "
        f"{valores[11]:>2}  {valores[10]:>2}"
    )

def circuito_da_expressao():
    separador()
    print("EXPRESSÃO BOOLEANA → CIRCUITO LÓGICO")
    print("=" * 70)

    print("""
Use:
* = AND
+ = OR
! = NOT

Exemplo:

(A * B) + !C
""")

    expressao = input("\nDigite a expressão: ").strip().upper()

    print("\nRepresentação do circuito:")
    print("=" * 70)

    construir_circuito(expressao)


def construir_circuito(expressao):

    expressao = expressao.replace(" ", "")

    contador_and = 0
    contador_or = 0
    contador_not = 0

    # NOT
    for match in re.finditer(r'!([A-Z])', expressao):
        contador_not += 1
        print(f"NOT{contador_not}: NOT({match.group(1)})")

    # AND
    for match in re.finditer(r'([A-Z0-9!()]+)\*([A-Z0-9!()]+)', expressao):
        contador_and += 1
        print(
            f"AND{contador_and}: "
            f"AND({match.group(1)}, {match.group(2)})"
        )

    # OR
    for match in re.finditer(r'([A-Z0-9!()]+)\+([A-Z0-9!()]+)', expressao):
        contador_or += 1
        print(
            f"OR{contador_or}: "
            f"OR({match.group(1)}, {match.group(2)})"
        )

    print("\nSaída final:")
    print(f"F = {expressao}")

    print("""
Fluxo lógico:

Entradas → Portas NOT/AND → Portas OR → Saída F
""")
def circuito_para_expressao():

    separador()
    print("CIRCUITO LÓGICO → EXPRESSÃO BOOLEANA")
    print("=" * 70)

    print("""
Informe as portas uma por uma.

Exemplo de circuito:

A ----\
       AND ----\
B ----/         \
                OR ---- F
C --------------/

Resultado:

F = (A * B) + C
""")

    quantidade = int(input("Quantidade de portas: "))

    sinais = {}

    for i in range(quantidade):

        print(f"\nPorta {i + 1}")

        tipo = input(
            "Tipo (AND, OR, NOT, NAND, NOR, XOR, XNOR): "
        ).upper()

        saida = input("Nome da saída: ").upper()

        if tipo == "NOT":
            entrada = input("Entrada: ").upper()

            sinais[saida] = f"!({entrada})"

        else:
            entrada1 = input("Entrada 1: ").upper()
            entrada2 = input("Entrada 2: ").upper()

            operadores = {
                "AND": "*",
                "OR": "+",
                "NAND": "NAND",
                "NOR": "NOR",
                "XOR": "XOR",
                "XNOR": "XNOR"
            }

            operador = operadores.get(tipo)

            if operador is None:
                print("Tipo inválido.")
                return

            sinais[saida] = (
                f"{operador}({entrada1}, {entrada2})"
            )

    print("\nExpressões das portas:")

    for saida, expressao in sinais.items():
        print(f"{saida} = {expressao}")

    print("\nExpressão final:")
    ultima_saida = list(sinais.keys())[-1]

    expressao_final = sinais[ultima_saida]

    mudou = True

    while mudou:

        mudou = False

        for nome, expressao in sinais.items():

            if nome != ultima_saida and nome in expressao:

                expressao_final = expressao_final.replace(
                    nome,
                    f"({expressao})"
                )

                mudou = True

    print(f"F = {expressao_final}")

def menu_principal():

    while True:

        separador()

        print("CALCULADORA DE SISTEMAS DIGITAIS")
        print("=" * 70)

        print("""
1  - Conversão de bases
2  - Códigos digitais
3  - Operações com bases numéricas
4  - Portas lógicas
5  - Tabela verdade
6  - Álgebra Booleana
7  - Mapa de Karnaugh
8  - Expressão → Circuito lógico
9  - Circuito lógico → Expressão
10 - Simplificação lógica
0  - Sair
""")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            conversao_bases()

        elif opcao == "2":
            menu_codigos()

        elif opcao == "3":
            operacoes_bases()

        elif opcao == "4":
            portas_logicas()

        elif opcao == "5":
            tabela_verdade()

        elif opcao == "6":
            algebra_booleana()

        elif opcao == "7":
            karnaugh()

        elif opcao == "8":
            circuito_da_expressao()

        elif opcao == "9":
            circuito_para_expressao()

        elif opcao == "10":
            expressao = input(
                "Digite a expressão booleana: "
            ).upper()

            print(
                "Simplificada:",
                simplificar_expressao(expressao)
            )

        elif opcao == "0":
            print("\nPrograma encerrado.")
            break

        else:
            print("Opção inválida.")

        input("\nPressione ENTER para continuar...")

if __name__ == "__main__":
    menu_principal()