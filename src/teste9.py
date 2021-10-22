"""
### BlastOff - Teste de Lógica 9 ###
Descrição: Mostra a tabuada de determinado número
Autor: Felipe Santana
Data: 22/10/2021
"""

# Mostra a tabuada de determinado número
def mostrar_tabuada(numero, multiplicador_maximo):
    for i in range(multiplicador_maximo + 1):
        produto = numero * i
        print(f'{numero} x {i} = {produto}')

# função main
def main():
    print('### Tabuada ###\n')

    numero = int(input('Digite um número inteiro: '))
    multiplicador = int(input('Digite o multiplicador máximo: '))

    mostrar_tabuada(numero, multiplicador)

if __name__ == '__main__':
    main()

