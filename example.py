OK_RESULT = 'yes'
FATAL_RESULT = 'no'
PEPE = 9
PLAYERS = []
CONTO = 200000  # Supongo un valor inicial para CONTO, puedes ajustarlo según lo necesites.

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

def pay_referee_taxes():
    def check_conto():
        return CONTO

    if check_conto() > 100000:
        global CONTO
        CONTO -= 100000

def add_players_to_list():
    while len(PLAYERS) < 11:
        r = input('Dime un jugador del madrid: ')
        if isinstance(r, str):
            PLAYERS.append(r)

# Ejecución del programa
#check_if_approve_or_not()
#pay_referee_taxes()
#add_players_to_list()
