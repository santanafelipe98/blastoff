"""
### BlastOff - Teste de Lógica 2 ###
Descrição: Dada a distância A e o combustível gasto B, calcula o consumo
Autor: Felipe Santana
Data: 21/10/2021
"""

# calcula o consumo medio de um veículo
def consumo_medio(distancia, combustivel_gasto):
    return distancia / combustivel_gasto

# função main
def main():
    distancia = float(input('Qual a distância percorrida (KM)? '))
    combustivel_gasto = float(input('Quanto de combustível foi gasto (L)? '))

    consumo = consumo_medio(distancia, combustivel_gasto)
    print('O consumo médio do veículo é {:.2f} KM por litro'.format(consumo))


if __name__ == '__main__':
    main()