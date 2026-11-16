"""
Lógica de los puntos: calcular la puntuación y detectar el blackjack natural.

Esta carpeta (logica) NO usa tkinter: aquí no hay nada visual.
"""

def calcularPuntos(mano: list) -> int:
  """
    Calcular los puntos que tiene una mano.

    Parameters:

      mano(list): Lista de cartas del jugador o dealer.

    Returns:

      int: Puntuación total de la mano.

    Examples:

      >>> calcularPuntos([("2", "♥"), ("7", "♥")])
      9

      >>> calcularPuntos([("A", "♦"), ("9", "♣"), ("9", "♠")])
      19
  """
  if not isinstance(mano, list):
    raise TypeError("La mano debe ser una lista.")

  puntos = 0
  ases = 0

  for carta in mano:
    if not isinstance(carta, tuple) or len(carta) != 2:
      raise ValueError("Cada carta debe tener valor y palo.")

    valor = carta[0]

    if valor == "A":
      puntos += 11
      ases += 1

    elif valor in ["J", "Q", "K"]:
      puntos += 10

    elif valor in ["2", "3", "4", "5", "6", "7", "8", "9", "10"]:
      puntos += int(valor)

    else:
      raise ValueError("Valor de carta no válido.")

  # Si nos pasamos de 21, cada As pasa de valer 11 a valer 1 (restamos 10) hasta que ya no nos pasemos o no queden ases por convertir
  while puntos > 21 and ases > 0:
    puntos -= 10
    ases -= 1

  return puntos

def blackJackNatural(mano: list) -> bool:
  """
    Comprobar si una mano tiene Blackjack natural.

    Parameters:

      mano(list): Lista de cartas del jugador o dealer.

    Returns:

      bool: True si tiene un As y una carta de valor 10 (10, J, Q, K) y False
      en caso contrario.

    Examples:

      >>> blackJackNatural([("A", "♣"), ("Q", "♠")])
      True

      >>> blackJackNatural([("A", "♦"), ("A", "♥")])
      False
  """
  # Blackjack natural: solo cuenta si son exactamente 2 cartas
  if len(mano) != 2:
    return False

  valores = [carta[0] for carta in mano]

  if "A" in valores and ("10" in valores or "J" in valores or "Q" in valores or "K" in valores):
    return True

  return False
