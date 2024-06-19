def inicializar_tablero():
    """Inicializa un tablero vacío de 3x3."""
    return [[' ' for _ in range(3)] for _ in range(3)]

def imprimir_tablero(tablero):
    """Imprime el tablero actual."""
    for fila in tablero:
        print('| ' + ' | '.join(fila) + ' |')
        print('-------------')

def hacer_movimiento(tablero, fila, columna, jugador):
    """Coloca la ficha del jugador en la fila y columna especificadas."""
    if tablero[fila][columna] == ' ':
        tablero[fila][columna] = jugador
        return True
    else:
        print("Esa posición ya está ocupada. Inténtalo de nuevo.")
        return False

def verificar_ganador(tablero, jugador):
    """Verifica si el jugador especificado ha ganado."""
    for i in range(3):
        # Verificar filas y columnas
        if all(tablero[i][j] == jugador for j in range(3)) or \
           all(tablero[j][i] == jugador for j in range(3)):
            return True

    # Verificar diagonales
    if all(tablero[i][i] == jugador for i in range(3)) or \
       all(tablero[i][2-i] == jugador for i in range(3)):
        return True

    return False

def tablero_lleno(tablero):
    """Verifica si el tablero está lleno (empate)."""
    for fila in tablero:
        if ' ' in fila:
            return False
    return True

def juego_michi():
    tablero = inicializar_tablero()
    jugadores = ['∂', '∫']
    jugador_actual = 0
    ganador = None

    while not ganador:
        imprimir_tablero(tablero)
        jugador = jugadores[jugador_actual]
        print(f'Turno del jugador {jugador}')
        
        fila = int(input('Selecciona la fila (0, 1, 2): '))
        columna = int(input('Selecciona la columna (0, 1, 2): '))
        
        if hacer_movimiento(tablero, fila, columna, jugador):
            if verificar_ganador(tablero, jugador):
                ganador = jugador
            elif tablero_lleno(tablero):
                ganador = 'Empate'
            jugador_actual = 1 - jugador_actual  # Cambiar turno

    imprimir_tablero(tablero)
    if ganador == 'Empate':
        print("¡Hubo un empate!")
    else:
        print(f"¡El jugador {ganador} ha ganado!")

# Para iniciar el juego, llama a la función juego_michi()
juego_michi()