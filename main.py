import pkg


"""def game_status():
        # Mostrar puntajes de la ronda actual
        print("Ronda:", ronda)
        print("Puntaje acumulado del usuario:", puntaje_usuario)
        print("Puntaje acumulado de la estrategia:", puntaje_estrategia)
        print()"""


def jugada(name, user_history):
    print(f'\n {name} ingresa O para cooperar o X para no cooperar')

    
    user_choise = input('==> ').upper()
    estatega_choise = pkg.tit_for_tat.t4t_strategy(user_history)

    return user_choise, estatega_choise


def puntaje(jugada_usuario, jugada_estratega, puntos_usuario, puntos_estratega):
    tabla_de_puntos = {
        ('X', 'X'): (1, 1),
        ('X', 'O'): (5, 0),
        ('O', 'X'): (0, 5),
        ('O', 'O'): (3, 3)
    }

    # Obtener el puntaje correspondiente para la jugada actual
    puntaje_actual = tabla_de_puntos[(jugada_usuario, jugada_estratega)]

    # Sumar los puntos de la jugada actual a los acumulados
    puntos_usuario += puntaje_actual[0]
    puntos_estratega += puntaje_actual[1]

    return puntos_usuario, puntos_estratega


def usuario():
    name = input('Ingresa tu nombre de jugador ==> ')
    return name


def main():

    name_usuario = usuario()
    puntaje_usuario = 0
    puntaje_estratega = 0
    historial_usuario = []
    historial_estratega = []
    ronda_maxima = pkg.random.randint(10, 20)
    turno = 0

    while turno != ronda_maxima:

        jugada_usuario,jugada_estratega = jugada(name_usuario, historial_usuario)

        historial_usuario.append(jugada_usuario)
        historial_estratega.append(jugada_estratega)

        print(historial_usuario)
        print(historial_estratega)

        puntaje_usuario, puntaje_estratega = puntaje(
            jugada_usuario, jugada_estratega,
            puntaje_usuario, puntaje_estratega
            )
        print(puntaje_usuario)
        print(puntaje_estratega)
        turno += 1


if __name__ == "__main__":
    main()
