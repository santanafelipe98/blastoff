"""
### BlastOff - Teste de Lógica 13 ###
Descrição: Imprime todos os valores de uma matriz de duas dimensões
Autor: Felipe Santana
Data: 22/10/2021
"""
# imprime valores da matriz
def imprimir_matriz(matriz):
    for i in range(len(matriz)):
        linha = ''
        for j in range(len(matriz[i])):
            val = matriz[i][j]
            linha += str(val) + ' '

        print(linha)

# função main
def main():
    matriz = [ [ 0, 2, 4 ], [ 20, 15, 3 ], [ 10, 1, 4, 0 ] ]
    imprimir_matriz(matriz)

if __name__ == '__main__':
    main()