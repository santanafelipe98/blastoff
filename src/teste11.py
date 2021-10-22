"""
### BlastOff - Teste de Lógica 11 ###
Descrição: Dada duas listas de números A[1,2,3,4] e B[1,2,5,8] retorna a intersecção das listas
Autor: Felipe Santana
Data: 22/10/2021
"""

# retorna a intersecção de duas listas de números
def interseccao(lista_valores1, lista_valores2):
    intersec = []

    for num in lista_valores1:
        if num in lista_valores2:
            intersec.append(num)
    
    return intersec

# função main
def main():
    lista_valores1 = [ 1, 2, 3, 4 ]
    lista_valores2 = [ 1, 2, 5, 8 ]
    _interseccao = interseccao(lista_valores1, lista_valores2)

    print(f'A = {lista_valores1}')
    print(f'B = {lista_valores2}')
    print(f'A ∩ B = {_interseccao}')

if __name__ == '__main__':
    main()

