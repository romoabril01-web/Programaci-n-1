"""
Lógica del mazo: crear el mazo y repartir cartas.

Esta carpeta (logica) NO usa tkinter: aquí no hay nada visual.
Biblioteca usada: random (para mezclar el mazo).
"""

import random

def crearMazo() -> list:
  """
    Crear un mazo de 52 cartas y mezclarlo.

    Returns:

      list: Lista de cartas, que contiene un valor y un palo.
  """
  palos = ["♥", "♦", "♣", "♠"]
  valores = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

  mazo = []

  for palo in palos:
    for valor in valores:
      mazo.append((valor, palo))

  random.shuffle(mazo)
  return mazo

def repartirCarta(mazo: list, mano: list) -> None:
  """
    Pasar una carta del mazo a la mano del jugador o del dealer.

    Parameters:

      mazo(list): Lista de cartas disponibles.
      mano(list): Lista de cartas del jugador o dealer.

    Returns:

      None: Agrega una carta a la mano.

    Raises:

      TypeError: Si los argumentos no son listas.
      ValueError: Si el mazo está vacío.
  """
  if not isinstance(mazo, list):
    raise TypeError("El mazo debe ser una lista.")
  if not isinstance(mano, list):
    raise TypeError("La mano debe ser una lista.")

  if len(mazo) == 0:
    raise ValueError("No quedan cartas en el mazo.")

  carta = mazo.pop()
  mano.append(carta)
