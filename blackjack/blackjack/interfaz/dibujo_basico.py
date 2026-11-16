"""
Dibujos básicos que usan las demás partes de la interfaz.

Biblioteca usada: tkinter (Canvas: create_polygon y create_text).
"""

import tkinter as tk

def rectRedondeado(canvas: tk.Canvas, x1: int, y1: int, x2: int, y2: int, r: int, fill: str, outline: str, width: int = 1) -> int:
  """
    Dibujar un rectángulo con las esquinas redondeadas.

    Parameters:

      canvas(tk.Canvas): Área donde se dibujará el rectángulo.
      x1, y1(int): Esquina superior izquierda.
      x2, y2(int): Esquina inferior derecha.
      r(int): Radio de las esquinas.
      fill(str): Color de relleno.
      outline(str): Color del borde.
      width(int): Grosor del borde.

    Returns:

      int: Identificador del polígono creado.
  """
  puntos = [x1 + r, y1, x2 - r, y1, x2, y1, x2, y1 + r, x2, y2 - r, x2, y2, x2 - r, y2, x1 + r, y2, x1, y2, x1, y2 - r, x1, y1 + r, x1, y1]
  return canvas.create_polygon(puntos, smooth=True, fill=fill, outline=outline, width=width)

def dibujarTexto(canvas: tk.Canvas, texto: str, x: int, y: int, ancla: str, fuente: tuple, color: str) -> None:
  """
    Dibujar un texto en el canvas.

    Parameters:

      canvas(tk.Canvas): Área donde se dibujará el texto.
      texto(str): Texto a mostrar.
      x, y(int): Posición del texto.
      ancla(str): "w" (alinear a la izquierda), "e" (a la derecha)
      o "center" (centrado).
      fuente(tuple): Fuente del texto.
      color(str): Color del texto.

    Returns:

      None: Dibuja el texto en el canvas.
  """
  canvas.create_text(x, y, text=texto, anchor=ancla, fill=color, font=fuente)
