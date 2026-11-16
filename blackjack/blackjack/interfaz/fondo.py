"""
Dibujo del fondo de la mesa: color verde, título, palos y marco.

Biblioteca usada: tkinter (Canvas: create_rectangle, create_line y create_text).
"""

import tkinter as tk

from interfaz.constantes import (ANCHO, ALTO_MESA, FUENTE_TITULO, COLOR_FONDO, DORADO, DORADO_OSCURO, CREMA, PALO_ROJO_TITULO, SOMBRA_TITULO)
from interfaz.dibujo_basico import rectRedondeado, dibujarTexto

def dibujarFondoVerde(canvas: tk.Canvas) -> None:
  """
    Pintar todo el canvas de verde.

    Parameters:

      canvas(tk.Canvas): Área donde se dibujará.

    Returns:

      None: Dibuja el rectángulo de fondo.
  """
  canvas.create_rectangle(0, 0, ANCHO, ALTO_MESA, fill=COLOR_FONDO, outline=COLOR_FONDO)

def dibujarTitulo(canvas: tk.Canvas) -> None:
  """Dibujar el título BLACKJACK dorado con sombra.

  Parameters:

      canvas(tk.Canvas): Área donde se dibujará.

  Returns:

      None: Dibuja el título.
  """
  fuente = (FUENTE_TITULO, 42, "bold")
  dibujarTexto(canvas, "BLACKJACK", ANCHO // 2 + 3, 53, "center", fuente, SOMBRA_TITULO)
  dibujarTexto(canvas, "BLACKJACK", ANCHO // 2, 50, "center", fuente, DORADO)


def dibujarPalos(canvas: tk.Canvas) -> None:
  """
    Dibujar los cuatro palos decorativos a los lados del título.

    Parameters:

      canvas(tk.Canvas): Área donde se dibujará.

    Returns:

      None: Dibuja los palos.
  """
  fuente = ("Arial", 30)
  dibujarTexto(canvas, "♠", 125, 50, "center", fuente, CREMA)
  dibujarTexto(canvas, "♥", 170, 50, "center", fuente, PALO_ROJO_TITULO)
  dibujarTexto(canvas, "♦", ANCHO - 170, 50, "center", fuente, PALO_ROJO_TITULO)
  dibujarTexto(canvas, "♣", ANCHO - 125, 50, "center", fuente, CREMA)

def dibujarSeparador(canvas: tk.Canvas) -> None:
  """
    Dibujar la línea dorada con un rombo en el centro, debajo del título.

    Parameters:

      canvas(tk.Canvas): Área donde se dibujará.

    Returns:

      None: Dibuja el separador.
  """
  canvas.create_line(60, 100, ANCHO // 2 - 20, 100, fill=DORADO_OSCURO, width=2)
  canvas.create_line(ANCHO // 2 + 20, 100, ANCHO - 60, 100, fill=DORADO_OSCURO, width=2)
  dibujarTexto(canvas, "◆", ANCHO // 2, 100, "center", ("Arial", 14), DORADO)


def dibujarMarco(canvas: tk.Canvas) -> None:
  """
    Dibujar el marco dorado alrededor de la mesa.

    Parameters:

      canvas(tk.Canvas): Área donde se dibujará.

    Returns:

      None: Dibuja el marco.
  """
  rectRedondeado(canvas, 18, 122, ANCHO - 18, ALTO_MESA - 18, 24, "", DORADO_OSCURO, 2)

def dibujarFondo(canvas: tk.Canvas) -> None:
  """
    Dibujar el fondo completo, uniendo las partes de este archivo.

    Parameters:

      canvas(tk.Canvas): Área donde se dibujará.

    Returns:

      None: Dibuja fondo, título, palos, separador y marco.
  """
  dibujarFondoVerde(canvas)
  dibujarTitulo(canvas)
  dibujarPalos(canvas)
  dibujarSeparador(canvas)
  dibujarMarco(canvas)
