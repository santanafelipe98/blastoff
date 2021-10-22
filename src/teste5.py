"""
### BlastOff - Teste de Lógica 5 ###
Descrição: Informa se dois números são multíplos
Autor: Felipe Santana
Data: 21/10/2021
"""

# retorna verdadeiro se os valor a for múltiplo de b
def eh_multiplo(a, b):
    return a % b == 0

def main():
    a = int(input('Digite um número inteiro: '))
    b = int(input('Digite mais um número inteiro: '))

    if eh_multiplo(a, b):
        print(f'{a} é múltiplo de {b}')
    else:
        print(f'{a} não é múltiplo de {b}')


if __name__ == '__main__':
    main()