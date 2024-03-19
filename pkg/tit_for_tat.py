def t4t_strategy(history):
    if len(history) < 2:
        return 'O'  # Cooperar en los dos primeros turnos
    elif history[-2:] == ['X', 'X']:
        return 'X'  # Dejar de cooperar si el oponente no coopera dos veces seguidas
    elif history[-1] == 'O' and history[-2] == 'X':
        return 'X'  # No volver a cooperar si el oponente coopera después de no cooperar
    else:
        # Hacer lo que hizo el oponente en el último turno
        return history[-1]
