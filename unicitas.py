
def reservar(disponibles, horario):
    if horario not in disponibles:
        return False

    disponibles.remove(horario)
    return True
