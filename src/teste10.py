"""
### BlastOff - Teste de Lógica 10 ###
Descrição: Calcula o fatorial de um número
Autor: Felipe Santana
Data: 22/10/2021
"""

# retorna o fatorial de um número
def fatorial(numero):
    fat = numero

    for i in range(numero, 1, -1):
        fat *= i - 1
    
    return fat

# função main
def main():
    numero = int(input('Digite um número inteiro: '))
    fat = fatorial(numero)

    print(f'O fatorial de {numero} é {fat}')

if __name__ == '__main__':
    main()