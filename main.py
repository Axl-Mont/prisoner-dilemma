import pkg
import time
import os

def clear_console():
    """Función para limpiar la consola"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_instrucciones():
    print("Bienvenido al Dilema del Prisionero\r")
    time.sleep(1)
    print("Este es un juego simple donde tú y una estrategia competirán en rondas.")
    time.sleep(1.5)
    print("Cada ronda, tienes que decidir si cooperar (O) o no cooperar (X).")
    time.sleep(1.5)
    print("Tu puntaje se determina según las decisiones tuyas y de la estrategia.")
    time.sleep(1.5)
    print("Si ambos cooperan    0 - 0 suman 3 puntos cada uno.")
    time.sleep(1.5)
    print("Si uno no coopera    X - 0 suman 5 puntos quien no coopera.")
    time.sleep(1.5)
    print("Si ambos no cooperan 0 - 0 suman 1 puntos cada uno.")
    time.sleep(1.5)
    print("El juego termina después de un número aleatorio de rondas entre 10 y 25.")
    time.sleep(1.5)
    print("¡Buena suerte y diviértete!")

def print_game_status(user_name, user_moves, strategy_moves):
    max_length = max(len(user_moves), len(strategy_moves))

    print("---------------------------------------------")
    print("                 Movimientos                 ")
    print("---------------------------------------------")

    user_moves_aligned = user_moves.ljust(max_length)
    strategy_moves_aligned = strategy_moves.ljust(max_length)

    len_t4t = len("Tit For Tat")
    len_user = len(user_name)
    user_spaces = " " * (len_t4t - len_user)

    print(f"{user_spaces}{user_name} {user_moves_aligned}")
    print(f"Tit For Tat {strategy_moves_aligned}")

def get_user_input(name, user_history):
    print(f'\n {name} ingresa O para cooperar o X para no cooperar')
    user_choice = input('==> ').upper()
    strategy_choice = pkg.tit_for_tat.t4t_strategy(user_history)
    return user_choice, strategy_choice

def calculate_score(user_choice, strategy_choice, user_score, strategy_score):
    score_table = {
        ('X', 'X'): (1, 1),
        ('X', 'O'): (5, 0),
        ('O', 'X'): (0, 5),
        ('O', 'O'): (3, 3)
    }
    current_score = score_table[(user_choice, strategy_choice)]
    user_score += current_score[0]
    strategy_score += current_score[1]
    return user_score, strategy_score

def main():
    clear_console()
    print_instrucciones()

    user_name = input('Ingresa tu nombre para comenzar ==> ').upper()
    user_score = 0
    strategy_score = 0
    user_history = []
    strategy_history = []
    round_max = pkg.random.randint(10, 25)
    round_count = 0

    user_moves = ''
    strategy_moves = ''

    while round_count < round_max:
        clear_console()
        print_game_status(user_name, user_moves, strategy_moves)

        user_choice, strategy_choice = get_user_input(user_name, user_history)
        user_history.append(user_choice)
        strategy_history.append(strategy_choice)

        user_moves = ''.join(user_history)
        strategy_moves = ''.join(strategy_history)

        user_score, strategy_score = calculate_score(user_choice, strategy_choice, user_score, strategy_score)

        round_count += 1

        if round_count >= round_max:
            break

if __name__ == "__main__":
    main()
