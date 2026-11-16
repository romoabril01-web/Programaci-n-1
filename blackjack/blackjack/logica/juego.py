"""
Lógica del juego: el estado de la partida y sus reglas.

Todo el estado de la partida vive en un diccionario llamado "juego":

    juego = {
      "mazo": [...],        # cartas que quedan
      "jugador": [...],     # cartas del jugador
      "dealer": [...],      # cartas del dealer
      "estado": "..."       # en qué momento está la partida (ver abajo)}

Valores posibles de "estado":

    "sin_iniciar"        -> todavía no se repartió
    "turno_jugador"      -> el jugador decide si pide carta o se planta
    "turno_dealer"       -> juega el dealer
    "jugador_blackjack"  -> terminó: blackjack natural solo del jugador
    "dealer_blackjack"   -> terminó: blackjack natural solo del dealer
    "empate_blackjack"   -> terminó: ambos tienen blackjack natural
    "jugador_pasa"       -> terminó: el jugador se pasó de 21
    "dealer_pasa"        -> terminó: el dealer se pasó de 21
    "jugador_gana"       -> terminó: el jugador tiene más puntos
    "dealer_gana"        -> terminó: el dealer tiene más puntos
    "empate"             -> terminó: misma puntuación

Esta carpeta (logica) no usa tkinter: aquí no hay nada visual.
"""

from logica.mazo import crearMazo, repartirCarta
from logica.puntos import calcularPuntos, blackJackNatural

ESTADOS_EN_CURSO = ["turno_jugador", "turno_dealer"]

def crearJuego() -> dict:
  """
    Crear el diccionario del juego, todavía sin repartir.

    Returns:

      dict: Diccionario con el mazo, las manos y el estado.
  """
  juego = {"mazo": [], "jugador": [], "dealer": [], "estado": "sin_iniciar"}
  return juego

def reiniciarJuego(juego: dict) -> None:
  """
    Preparar una partida nueva: mazo nuevo y manos vacías.

    Parameters:

      juego(dict): Diccionario del juego.

    Returns:

      None: Modifica el diccionario.
  """
  juego["mazo"] = crearMazo()
  juego["jugador"] = []
  juego["dealer"] = []
  juego["estado"] = "turno_jugador"

def repartirManoInicial(juego: dict) -> None:
  """
    Repartir las dos primeras cartas a cada uno.

    Parameters:

      juego(dict): Diccionario del juego.

    Returns:

      None: Agrega dos cartas al jugador y dos al dealer.
  """
  # Se reparte de una en una, alternando: jugador, dealer, jugador, dealer
  repartirCarta(juego["mazo"], juego["jugador"])
  repartirCarta(juego["mazo"], juego["dealer"])
  repartirCarta(juego["mazo"], juego["jugador"])
  repartirCarta(juego["mazo"], juego["dealer"])

def detectarBlackjackNatural(juego: dict) -> str:
  """
    Revisar si alguien tiene blackjack natural al repartir.

    Parameters:

      juego(dict): Diccionario del juego.

    Returns:

      str: "jugador_blackjack", "dealer_blackjack", "empate_blackjack" o "" si nadie tiene blackjack natural.
  """
  jugadorBlackjack = blackJackNatural(juego["jugador"])
  dealerBlackjack = blackJackNatural(juego["dealer"])

  if jugadorBlackjack and dealerBlackjack:
    return "empate_blackjack"
  if jugadorBlackjack:
    return "jugador_blackjack"
  if dealerBlackjack:
    return "dealer_blackjack"
  return ""

def terminarPartida(juego: dict, resultado: str) -> None:
  """
    Cerrar la partida guardando cómo terminó.

    Parameters:

      juego(dict): Diccionario del juego.
      resultado(str): Uno de los estados finales (por ejemplo "empate").

    Returns:

      None: Cambia el estado del juego.
  """
  juego["estado"] = resultado

def iniciarPartida(juego: dict) -> None:
  """
    Empezar una nueva partida: reparte y revisa el blackjack natural.

    Parameters:

      juego(dict): Diccionario del juego.

    Returns:

      None: Deja el juego listo para jugar o ya terminado si hay blackjack.
  """
  reiniciarJuego(juego)
  repartirManoInicial(juego)

  resultado = detectarBlackjackNatural(juego)
  if resultado != "":
    terminarPartida(juego, resultado)

def partidaTerminada(juego: dict) -> bool:
  """
    Saber si la partida ya terminó.

    Returns:

      bool: True si ya hay un resultado (o si todavía no se inició).
  """
  return juego["estado"] not in ESTADOS_EN_CURSO

def esTurnoJugador(juego: dict) -> bool:
  """
    Saber si le toca decidir al jugador.

    Returns:

      bool: True si el estado es "turno_jugador".
  """
  return juego["estado"] == "turno_jugador"

def dealerEstaOculta(juego: dict) -> bool:
  """
    Saber si la segunda carta del dealer debe verse tapada.

    Returns:

      bool: True solo mientras es el turno del jugador.
  """
  return juego["estado"] == "turno_jugador"

def jugadorPideCarta(juego: dict) -> None:
  """
    Darle una carta más al jugador.

    Returns:

      None: Agrega una carta a la mano del jugador.
  """
  repartirCarta(juego["mazo"], juego["jugador"])

def jugadorSePaso(juego: dict) -> bool:
  """
    Saber si el jugador se pasó de 21.

    Returns:

      bool: True si el jugador tiene más de 21 puntos.
  """
  return calcularPuntos(juego["jugador"]) > 21

def pasarTurnoAlDealer(juego: dict) -> None:
  """
    Terminar el turno del jugador (se planta) y empezar el del dealer.

    Returns:

      None: Cambia el estado a "turno_dealer".
  """
  juego["estado"] = "turno_dealer"

def dealerDebePedir(juego: dict) -> bool:
  """
    Saber si el dealer está obligado a pedir carta.

    Returns:

      bool: True mientras el dealer tenga menos de 17 puntos.
  """
  # Regla del dealer: pide carta mientras tenga menos de 17 puntos
  return calcularPuntos(juego["dealer"]) < 17

def dealerPideCarta(juego: dict) -> None:
  """
    Darle una carta más al dealer.

    Returns:

      None: Agrega una carta a la mano del dealer.
  """
  repartirCarta(juego["mazo"], juego["dealer"])

def calcularResultado(juego: dict) -> str:
  """
    Decidir quién gana comparando los puntos.

    Parameters:

      juego(dict): Diccionario del juego.

    Returns:

      str: "jugador_pasa", "dealer_pasa", "jugador_gana", "dealer_gana"
      o "empate".
  """
  puntosJugador = calcularPuntos(juego["jugador"])
  puntosDealer = calcularPuntos(juego["dealer"])

  # El orden importa: primero se revisa si alguien se pasó de 21 y después se comparan los puntos
  if puntosJugador > 21:
    return "jugador_pasa"
  if puntosDealer > 21:
    return "dealer_pasa"
  if puntosJugador > puntosDealer:
    return "jugador_gana"
  if puntosJugador < puntosDealer:
    return "dealer_gana"
  return "empate"
