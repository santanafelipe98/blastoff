"""
### BlastOff - Teste de Lógica 12 ###
Descrição: Dada duas listas de números A[1,2,3,4] e B[1,2,5,8] retorna a concatenação das listas
Autor: Felipe Santana
Data: 22/10/2021
"""

# retorna a união de duas listas
def uniao(lista_numeros1, lista_numeros2):
    nova_lista = lista_numeros1 + lista_numeros2
    return nova_lista

# função main
def main():
    lista_valores1 = [ 1, 2, 3, 4 ]
    lista_valores2 = [ 1, 2, 5, 8 ]
    _uniao = uniao(lista_valores1, lista_valores2)

    print(f'A = {lista_valores1}')
    print(f'B = {lista_valores2}')
    print(f'A U B = {_uniao}')

if __name__ == '__main__':
    main()