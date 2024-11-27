OK_RESULT = 'yes'
FATAL_RESULT = 'no'
PEPE = 9
PLAYERS = []

def check_if_approve_or_not() -> str:
    result = input('¿Eres del Madrid? ')

    if isinstance(result, str):
        if result.lower() == 'yes':
            return "Aprobado"
        for i in range(0, 15):
            r = input('¿Estás seguro? ')
            if isinstance(r, str) and r == 'yes':
                return "SUSPENDIDO"
    return "SUSPENDIDO"

def add_players_to_list():
    while len(PLAYERS) < 11:
        r = input('Dime un jugador del madrid: ')
        if isinstance(r, str):
            PLAYERS.append(r)

check_if_approve_or_not()
add_players_to_list()
