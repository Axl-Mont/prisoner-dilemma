import pkg

player = []
ia = []

def puntaje(jugada_usuario, jugada_estrategia, puntos_usuario, puntos_estrategia):
    tabla_de_puntos = {
        ('X', 'X'): (3, 3),
        ('X', 'O'): (5, 0),
        ('O', 'X'): (0, 5),
        ('O', 'O'): (1, 1)
    }

    # Obtener el puntaje correspondiente para la jugada actual
    puntaje_actual = tabla_de_puntos[(jugada_usuario, jugada_estrategia)]

    # Sumar los puntos de la jugada actual a los acumulados
    puntos_usuario += puntaje_actual[0]
    puntos_estrategia += puntaje_actual[1]

    return puntos_usuario, puntos_estrategia

def main():
    # Inicializar puntajes
    puntaje_usuario = 0
    puntaje_estrategia = 0

    # Inicializar contador de rondas
    ronda = 1

    # Ejemplo de uso
    while ronda <= 10:  # Por ejemplo, 10 rondas
        # Simular jugadas
        jugada_usuario = 'X'
        jugada_estrategia = 'O'

        # Calcular puntajes de la ronda actual
        puntaje_usuario, puntaje_estrategia = puntaje(jugada_usuario, jugada_estrategia, puntaje_usuario, puntaje_estrategia)

        # Mostrar puntajes de la ronda actual
        print("Ronda:", ronda)
        print("Puntaje acumulado del usuario:", puntaje_usuario)
        print("Puntaje acumulado de la estrategia:", puntaje_estrategia)
        print()

        # Incrementar contador de rondas
        ronda += 1

if __name__ == "__main__":
    main()
