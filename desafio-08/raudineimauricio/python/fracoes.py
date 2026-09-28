"""
Lê um arquivo texto com uma fração por linha (formato "a/b" ou apenas "a")
e imprime a versão simplificada de cada uma.

Regras:
- Números simples (sem "/") são tratados como fração de denominador 1.
- Frações cujo resultado é inteiro (ex: 81/9) imprimem apenas o inteiro.
- Frações impróprias (numerador > denominador) são impressas como número
  misto: "parte_inteira resto/denominador".
- Frações próprias são impressas como "numerador/denominador" já simplificado.
- Qualquer erro (divisão por zero, formato inválido, etc.) imprime "ERR".
"""
import sys

def mdc(a: int, b: int) -> int:

    """
    Calculamos o Máximo Divisor Comum MDC entre dois números.

    """
    a, b = abs(a), abs(b)
    while b:                # Loop enquanto "b" for diferente de zero
        a, b = b, a % b      # "%" é o resto da divisão de a por b
    return a


def processa_linha(linha: str) -> str:

    """
    Recebe uma linha de texto e devolve o texto já formatado
    """
    linha = linha.strip()

    # Verificamos se o texto não está em um formato difente(letras, símbolos, etc.)
    # e caso tenha erro, o programa não trava.
    try:
        if "/" in linha:

            partes = linha.split("/")

            if len(partes) != 2:
                return "ERR"

            numerador = int(partes[0])
            denominador = int(partes[1])

        else:

            numerador = int(linha)
            denominador = 1

        if denominador == 0:
            return "ERR"

        if denominador < 0:
            numerador, denominador = -numerador, -denominador


        divisor_comum = mdc(numerador, denominador)
        numerador //= divisor_comum
        denominador //= divisor_comum

        if denominador == 1:

            return str(numerador)

        sinal = "-" if numerador < 0 else ""
        numerador_abs = abs(numerador)

        inteiro, resto = divmod(numerador_abs, denominador)

        if inteiro == 0:

            return f"{sinal}{resto}/{denominador}"

        return f"{sinal}{inteiro} {resto}/{denominador}"

    except ValueError:
        # Cai aqui se int() não conseguiu converter o texto em número:
        # por exemplo, uma linha com letras ou vazia sem ser detectada antes.
        return "ERR"

def main():
    """
    Função principal: decide de onde ler as frações (arquivo passado como
    argumento, arquivo padrão "frac.txt" ou entrada redirecionada) e chama
    processa_linha() para cada linha, imprimindo o resultado.
    """

    if len(sys.argv) > 1:
        caminho = sys.argv[1]

    elif sys.stdin.isatty():

        caminho = "frac.txt"

    else:
        caminho = None

    if caminho:
        # Abrimos o arquivo e validamos se ele será fechado , mesmo em caso de erro.

        with open(caminho, "r", encoding="utf-8") as f:
            linhas = f.readlines()

    else:
        linhas = sys.stdin.readlines()

    # Aqui percorremos cada linha do arquivo.
    for linha in linhas:

        if linha.strip() == "":
            # Se tiver Linha em branco, pula para a próxima linha sem imprimir
            continue

        print(processa_linha(linha))


if __name__ == "__main__":
    main()
