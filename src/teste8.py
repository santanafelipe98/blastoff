"""
### BlastOff - Teste de Lógica 8 ###
Descrição: Informa se o número é primo ou não
Autor: Felipe Santana
Data: 22/10/2021
"""

# retorna verdadeiro se o número for primo
def eh_primo(numero):
    primo = True

    if numero == 1 or numero == 2:
        return True
    
    for i in range(2, numero - 1):
        if numero % i == 0:
            primo = False
            break

    return primo

# função main
def main():
    numero = int(input('Digite um número inteiro: '))
    
    if eh_primo(numero):
        print(f'{numero} é primo')
    else:
        print(f'{numero} não é primo')

if __name__ == '__main__':
    main()