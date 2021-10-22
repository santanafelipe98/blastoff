"""
### BlastOff - Teste de Lógica 4 ###
Descrição: Converte a temperatura de Celsius para Fahrenheit
Autor: Felipe Santana
Data: 21/10/2021
"""

# converte celsius em fahrenheit
def celsius_fahrenheit(celsius):
    return celsius * (9 / 5) + 32

# função main
def main():
    celsius = float(input('Digite a temperatura em graus Celsius: '))
    fahrenheit = celsius_fahrenheit(celsius)

    print(f'{celsius} °C é o mesmo que {fahrenheit} F')

if __name__ == '__main__':
    main()