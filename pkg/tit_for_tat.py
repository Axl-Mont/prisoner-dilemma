import pkg  #
def t4t_strategy(history):
    options = ['X', 'O']
    limit = len(options)

    if len(history) < 2:
        return 'O'  # Cooperar en los dos primeros turnos
    elif history[-2:] == ['X', 'X']:
        return 'X'  # Dejar de cooperar si el oponente no coopera dos veces seguidas
    elif history[-2:] == ['O', 'O']:
        return 'O'  # Volver a cooperar si el oponente coopera después de no cooperar
    else:
        # Hacer un movimiento aleatorio
        choise = options[pkg.random.randint(0, limit) -1]  # Acceder a random desde pkg
        return choise
