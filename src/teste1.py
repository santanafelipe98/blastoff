"""
### BlastOff - Teste de Lógica 1 ###
Descrição: Dadas as idades I, J, K, X, Y, calcula a média das idades
Autor: Felipe Santana
Data: 21/10/2021
"""

# calcula a média de uma lista de valores
def media(lista_valores):
    soma = sum(lista_valores)

    return soma / len(lista_valores)

# obtém as idades
def get_idades():
    identificacao_idades = [ 'I', 'J', 'K', 'X', 'Y' ]
    idades = []

    for i in range(len(identificacao_idades)):
        idade = int(input(f'Digite a idade de {identificacao_idades[i]}: '))
        idades.append(idade)
    
    return idades

# função main
def main():
    media_idades = media(get_idades())
    print(f'A média das idades é: {media_idades}')
    
if __name__ == '__main__':
    main()

