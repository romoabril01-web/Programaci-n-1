"""
Dibujo de la mesa completa: fondo, dealer, mensaje y jugador.

Biblioteca usada: tkinter (Canvas). Esta parte solo LEE el diccionario "juego" para saber qué dibujar; nunca lo modifica.
"""

import tkinter as tk

from interfaz.constantes import (ANCHO, FUENTE_TITULO, FUENTE_TEXTO, DORADO, COLOR_TEXTO, COLOR_FONDO_MENSAJE, MENSAJES)
from interfaz.dibujo_basico import rectRedondeado, dibujarTexto
from interfaz.fondo import dibujarFondo
from interfaz.cartas import dibujarMano
from logica.juego import dealerEstaOculta
from logica.puntos import calcularPuntos

def obtenerTextoPuntosDealer(juego: dict) -> str:
  """
    Armar el texto de los puntos del dealer.

    Parameters:

      juego(dict): Diccionario del juego.

    Returns:

      str: "Puntos: N" o "Puntos: N + ?" si hay una carta tapada.
  """
  if dealerEstaOculta(juego):
    # Mientras la segunda carta está tapada, solo se cuenta la primera
    puntos = calcularPuntos([juego["dealer"][0]])
    return f"Puntos: {puntos} + ?"
  return f"Puntos: {calcularPuntos(juego['dealer'])}"


def dibujarDealer(canvas: tk.Canvas, juego: dict) -> None:
  """
    Dibujar la zona del dealer: nombre, puntos y cartas.

    Parameters:

      canvas(tk.Canvas): Área donde se dibujará.
      juego(dict): Diccionario del juego.

    Returns:

      None: Dibuja la zona del dealer.
  """
  dibujarTexto(canvas, "DEALER", 50, 150, "w", (FUENTE_TITULO, 16, "bold"), DORADO)
  dibujarTexto(canvas, obtenerTextoPuntosDealer(juego), ANCHO - 50, 150, "e", (FUENTE_TEXTO, 14, "bold"), COLOR_TEXTO)
  dibujarMano(canvas, juego["dealer"], 172, dealerEstaOculta(juego))

def dibujarMensaje(canvas: tk.Canvas, juego: dict) -> None:
  """
    Dibujar el mensaje central según el estado del juego.

    Parameters:

      canvas(tk.Canvas): Área donde se dibujará.
      juego(dict): Diccionario del juego.

    Returns:

      None: Dibuja el cuadro con el mensaje (si hay mensaje).
  """
  texto, color = MENSAJES[juego["estado"]]

  if texto != "":
    rectRedondeado(canvas, ANCHO // 2 - 300, 318, ANCHO // 2 + 300, 362, 22, COLOR_FONDO_MENSAJE, DORADO, 2)
    dibujarTexto(canvas, texto, ANCHO // 2, 340, "center", (FUENTE_TITULO, 17, "bold"), color)

def dibujarJugador(canvas: tk.Canvas, juego: dict) -> None:
  """
    Dibujar la zona del jugador: nombre, puntos y cartas.

    Parameters:

      canvas(tk.Canvas): Área donde se dibujará.
      juego(dict): Diccionario del juego.

    Returns:

      None: Dibuja la zona del jugador.
  """
  puntos = calcularPuntos(juego["jugador"])
  dibujarTexto(canvas, "JUGADOR", 50, 392, "w", (FUENTE_TITULO, 16, "bold"), DORADO)
  dibujarTexto(canvas, f"Puntos: {puntos}", ANCHO - 50, 392, "e", (FUENTE_TEXTO, 14, "bold"), COLOR_TEXTO)
  dibujarMano(canvas, juego["jugador"], 412)

def dibujarMesa(canvas: tk.Canvas, juego: dict) -> None:
  """
    Borrar el canvas y dibujar toda la mesa otra vez.

    Parameters:

      canvas(tk.Canvas): Área donde se dibujará.
      juego(dict): Diccionario del juego.

    Returns:

      None: Actualiza todo lo que se ve en el canvas.
  """
  canvas.delete("all")
  dibujarFondo(canvas)
  dibujarDealer(canvas, juego)
  dibujarMensaje(canvas, juego)
  dibujarJugador(canvas, juego)
