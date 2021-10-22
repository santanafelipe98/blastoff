"""
### BlastOff - Teste de Lógica 3 ###
Descrição: Dados três números (a, b, c), exiba o menor número
Autor: Felipe Santana
Data: 21/10/2021
"""

# retorna o menor valor entre 3 números
def menor(a, b, c):
    if a < b and a < c:
        return a
    elif b < c:
        return b
    else:
        return c

# função main
def main():
    a = float(input('Digite o valor de A: '))
    b = float(input('Digite o valor de B: '))
    c = float(input('Digite o valor de C: '))

    m = menor(a, b, c)

    print(f'O menor valor é: {m}')

if __name__ == '__main__':
    main()