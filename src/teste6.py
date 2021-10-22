"""
### BlastOff - Teste de Lógica 6 ###
Descrição: Calcula a diferença de tempo entre hora inicial e hora final
Autor: Felipe Santana
Data: 21/10/2021
"""

class Tempo:
    def __init__(self, hora, minutos):
        self.hora = hora
        self.minutos = minutos
    
    # retorna um novo tempo representando a diferenca de tempo
    def diferenca(self, outro_tempo):
        tempo_minutos = (self.hora * 60) + self.minutos
        outro_tempo_minutos = (outro_tempo.hora * 60) + outro_tempo.minutos

        diferenca_minutos = abs(tempo_minutos - outro_tempo_minutos)
        diferenca_hora = diferenca_minutos / 60
        resto_minutos  = ((diferenca_minutos / 60) - (diferenca_minutos // 60)) * 60

        return Tempo(int(diferenca_hora), int(resto_minutos))

    # formata o tempo transformando-o em string
    def formatado(self):
        string_hora = str(self.hora)
        string_minutos = str(self.minutos)

        if self.hora < 10:
            string_hora = f'0{self.hora}'
        
        if self.minutos < 10:
            string_minutos = f'0{self.minutos}'

        return f'{string_hora}:{string_minutos}'


# converte string (H:m) para tempo
def string_para_tempo(string):
    horas = string.split(':')
    tempo = Tempo(int(horas[0]), int(horas[1]))

    return tempo

# obtém tempo
def get_tempo(prompt):
    string_tempo = input(prompt)
    return string_para_tempo(string_tempo)

# função main
def main():
    tempo_inicial = get_tempo('Que horas a partida iniciou (H:m)? ')
    tempo_final  = get_tempo('Que horas a partida finalizou (H:m)? ')

    tempo_diferenca = tempo_inicial.diferenca(tempo_final)
    string_tempo_diferenca = tempo_diferenca.formatado()

    print(f'A partida durou cerca de {string_tempo_diferenca} hs.')

if __name__ == '__main__':
    main()