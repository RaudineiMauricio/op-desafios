# Desafio 08 - Simplificador de frações (Python)

Programa que lê um arquivo de texto com uma fração por linha e imprime a
versão simplificada de cada uma.

## O que o programa faz.

Para cada linha do arquivo, o programa segue estas regras:

| Entrada | Regra aplicada | Saída |
|---------|----------------|-------|
| `14/3`  | Fração imprópria vira número misto | `4 2/3` |
| `4/8`   | Fração é simplificada | `1/2` |
| `3/8`   | Fração própria já simplificada não muda | `3/8` |
| `5`     | Número simples tem denominador 1, imprime só o número | `5` |
| `48/12` | Divisão exata imprime só o número inteiro | `4` |
| `10/0`  | Divisão por zero é erro | `ERR` |

Qualquer linha em formato inválido (letras, várias barras, etc.) também
imprime `ERR`. Linhas em branco são ignoradas.


## Como executar.

Passando o arquivo como argumento:

```bash
python3 fracoes.py frac.txt
```

Ou redirecionando a entrada:

```bash
python3 fracoes.py < frac.txt
```
Se o programa for executado sem argumento e sem redirecionamento, ele usa o
arquivo `frac.txt` da pasta atual.

No Windows, use `python` no lugar de `python3`, se for o caso.

## Como funciona

1. **Leitura:** cada linha é separada em numerador e denominador. Se não
   houver `/`, o denominador é 1.
2. **Erro:** se o denominador for 0 ou o texto não for um número válido,
   imprime `ERR`.
3. **Simplificação:** calcula o MDC (máximo divisor comum) com o algoritmo de
   Euclides e divide numerador e denominador por ele.
4. **Formato da saída:**
   - denominador 1: imprime só o número inteiro;
   - numerador menor que o denominador: imprime `numerador/denominador`;
   - numerador maior que o denominador: imprime número misto, como
     `4 2/3`.
