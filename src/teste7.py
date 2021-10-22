"""
### BlastOff - Teste de Lógica 7 ###
Descrição: Dada uma lista de números A[1,2,3,...] retorna somente os números pares
Autor: Felipe Santana
Data: 22/10/2021
"""

# filtra somente os números pares
def pares(lista_numeros):
    somente_pares = []

    for num in lista_numeros:
        if num % 2 == 0:
            somente_pares.append(num)
    
    return somente_pares

# função main
def main():
    numeros = [ 14, 5, 6, 7, 11, 20 ]
    somente_pares = pares(numeros)

    print(f'Lista de números: {numeros}')
    print(f'Números pares: {somente_pares}')



if __name__ == '__main__':
    main()