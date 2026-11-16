"""
Dibujo de las cartas y de las manos.

Biblioteca usada: tkinter (Canvas: create_oval y create_text, más los rectángulos redondeados de dibujo_basico.py).
"""

import tkinter as tk

from interfaz.constantes import (ANCHO, CARTA_W, CARTA_H, FUENTE_TITULO, CREMA, BORDE_CARTA, BORDO, DORADO, CARTA_NEGRA, CARTA_ROJA)
from interfaz.dibujo_basico import rectRedondeado, dibujarTexto

def dibujarBaseCarta(canvas: tk.Canvas, x: int, y: int) -> None:
  """
    Dibujar el fondo crema de una carta.

    Parameters:

      canvas(tk.Canvas): Área donde se dibujará.
      x(int): Posición horizontal.
      y(int): Posición vertical.

    Returns:

      None: Dibuja la base de la carta.
  """
  rectRedondeado(canvas, x, y, x + CARTA_W, y + CARTA_H, 10, CREMA, BORDE_CARTA)

def dibujarReverso(canvas: tk.Canvas, x: int, y: int) -> None:
  """
    Dibujar la parte de atrás de una carta (burdeos con borde dorado).

    Parameters:

      canvas(tk.Canvas): Área donde se dibujará.
      x(int): Posición horizontal.
      y(int): Posición vertical.

    Returns:

      None: Dibuja el reverso encima de la base.
  """
  rectRedondeado(canvas, x + 5, y + 5, x + CARTA_W - 5, y + CARTA_H - 5, 8, BORDO, DORADO, 2)
  dibujarTexto(canvas, "♠", x + CARTA_W / 2, y + CARTA_H / 2, "center", ("Arial", 20), DORADO)

def obtenerColorPalo(palo: str) -> str:
  """
    Decidir el color de una carta según su palo.

    Parameters:

      palo(str): "♠", "♣", "♥" o "♦".

    Returns:

      str: Color negro para ♠ y ♣, rojo para ♥ y ♦.
  """
  if palo in ["♠", "♣"]:
    return CARTA_NEGRA
  return CARTA_ROJA

def dibujarFrente(canvas: tk.Canvas, carta: tuple, x: int, y: int) -> None:
  """
    Dibujar el valor y el palo de una carta boca arriba.

    Parameters:

      canvas(tk.Canvas): Área donde se dibujará.
      carta(tuple): Valor y palo de la carta.
      x(int): Posición horizontal.
      y(int): Posición vertical.

    Returns:

      None: Dibuja los textos de la carta.
  """
  valor, palo = carta
  color = obtenerColorPalo(palo)
  fuenteValor = (FUENTE_TITULO, 16, "bold")

  dibujarTexto(canvas, valor, x + 10, y + 17, "w", fuenteValor, color)
  dibujarTexto(canvas, palo, x + 10, y + 37, "w", ("Arial", 14), color)
  dibujarTexto(canvas, palo, x + CARTA_W / 2, y + CARTA_H / 2 + 4, "center", ("Arial", 40), color)
  dibujarTexto(canvas, palo, x + CARTA_W - 10, y + CARTA_H - 37, "e", ("Arial", 14), color)
  dibujarTexto(canvas, valor, x + CARTA_W - 10, y + CARTA_H - 17, "e", fuenteValor, color)

def dibujarCarta(canvas: tk.Canvas, carta: tuple, x: int, y: int, oculta: bool = False) -> None:
  """
    Dibujar una carta, boca arriba o boca abajo.

    Parameters:

      canvas(tk.Canvas): Área donde se dibujará la carta.
      carta(tuple): Valor y palo de la carta.
      x(int): Posición horizontal.
      y(int): Posición vertical.
      oculta(bool): Indica si la carta estará oculta.

    Returns:

      None: Dibuja la carta en el canvas.
  """
  dibujarBaseCarta(canvas, x, y)

  if oculta:
    dibujarReverso(canvas, x, y)
  else:
    dibujarFrente(canvas, carta, x, y)

def calcularSeparacion(cantidad: int) -> int:
  """
    Calcular cuántos píxeles separan una carta de la siguiente.

    Si hay muchas cartas, se acercan para que quepan en la ventana.

    Parameters:

      cantidad(int): Número de cartas de la mano.

    Returns:

      int: Separación horizontal entre cartas.
  """
  return min(CARTA_W + 15, (ANCHO - 120 - CARTA_W) // max(cantidad - 1, 1))


def dibujarMano(canvas: tk.Canvas, mano: list, y: int, ocultarSegunda: bool = False) -> None:
  """Dibujar una mano completa centrada horizontalmente.

  Parameters:

      canvas(tk.Canvas): Área donde se dibujará.
      mano(list): Lista de cartas a dibujar.
      y(int): Posición vertical de la fila de cartas.
      ocultarSegunda(bool): Si es True, la segunda carta se dibuja boca abajo.

  Returns:

      None: Dibuja las cartas en el canvas.
  """
  separacion = calcularSeparacion(len(mano))
  anchoTotal = separacion * (len(mano) - 1) + CARTA_W
  x0 = (ANCHO - anchoTotal) // 2

  for i, carta in enumerate(mano):
    x = x0 + i * separacion
    dibujarCarta(canvas, carta, x, y, ocultarSegunda and i == 1)
