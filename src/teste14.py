"""
### BlastOff - Teste de Lógica 14 ###
Descrição: Recebe uma palavra e retorna se a mesma é um palíndromo
Autor: Felipe Santana
Data: 22/10/2021
"""

# retorna se a palavra é um palíndromo
def eh_palindromo(palavra):
    palavra_invertida = palavra[::-1]

    return palavra == palavra_invertida

# função main
def main():
    palavra = input('Digite uma palavra: ')
    palindromo = eh_palindromo(palavra)

    if palindromo:
        print(f'{palavra} é um palíndromo')
    else:
        print(f'{palavra} não é um palíndromo')

if __name__ == '__main__':
    main()