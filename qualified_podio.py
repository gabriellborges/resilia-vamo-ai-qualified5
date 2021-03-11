def podio_olimpico(tempo_chegada1, tempo_chegada2, tempo_chegada3):
    ordem = [tempo_chegada1, tempo_chegada2, tempo_chegada3]
    ordem_chegada = sorted(ordem)
    ordem_chegadaStr = ('1 - {} minutos\n2 - {} minutos\n3 - {} minutos\n').format(ordem_chegada[0], ordem_chegada[1], ordem_chegada[2])
    return ordem_chegadaStr