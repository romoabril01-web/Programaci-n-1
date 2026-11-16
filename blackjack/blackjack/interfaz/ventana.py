"""
Creación de la ventana, el canvas y los botones.

Biblioteca usada: tkinter (Tk, Canvas, Frame y Button).
"""

import tkinter as tk

from interfaz.constantes import (ANCHO, ALTO_MESA, FUENTE_TEXTO, COLOR_FONDO, COLOR_FONDO_BARRA, DORADO, DORADO_CLARO, CREMA, BORDO, BORDO_CLARO)

def crearVentana() -> tk.Tk:
  """
    Crear la ventana principal del juego.

    Returns:

      tk.Tk: La ventana, con título y tamaño fijo.
  """
  ventana = tk.Tk()
  ventana.title("BlackJack")
  ventana.resizable(False, False)
  return ventana

def crearCanvas(ventana: tk.Tk) -> tk.Canvas:
  """
    Crear el área donde se dibuja la mesa.

    Parameters:

      ventana(tk.Tk): Ventana donde se pondrá el canvas.

    Returns:

      tk.Canvas: El canvas ya colocado en la ventana.
  """
  canvas = tk.Canvas(ventana, width=ANCHO, height=ALTO_MESA, bg=COLOR_FONDO, highlightthickness=0)
  canvas.pack()
  return canvas

def crearBarraBotones(ventana: tk.Tk) -> tk.Frame:
  """
    Crear la barra inferior donde irán los botones.

    Parameters:

      ventana(tk.Tk): Ventana donde se pondrá la barra.

    Returns:

      tk.Frame: El contenedor donde se colocan los botones.
  """
  barra = tk.Frame(ventana, bg=COLOR_FONDO_BARRA)
  barra.pack(fill="x")

  contenedor = tk.Frame(barra, bg=COLOR_FONDO_BARRA)
  contenedor.pack(pady=16)
  return contenedor

def estilizarBoton(boton: tk.Button, fondo: str, texto: str, hover: str) -> None:
  """
    Dar color, letra y forma a un botón.

    Parameters:

      boton(tk.Button): Botón a modificar.
      fondo(str): Color de fondo.
      texto(str): Color de la letra.
      hover(str): Color cuando se hace clic.

    Returns:

      None: Modifica el botón.
  """
  boton.config(bg=fondo, fg=texto, activebackground=hover, activeforeground=texto, disabledforeground="#8a8a6a", relief="flat", bd=0, cursor="hand2", font=(FUENTE_TEXTO, 13, "bold"), width=14, pady=8)

def activarHover(boton: tk.Button, fondo: str, hover: str) -> None:
  """
    Hacer que el botón cambie de color al pasar el ratón por encima.

    Parameters:

      boton(tk.Button): Botón a modificar.
      fondo(str): Color normal.
      hover(str): Color cuando el ratón está encima.

    Returns:

      None: Conecta los eventos del ratón al botón.
  """
  # bind sirve para ejecutar algo cuando pasa un evento con el mouse.
  # <Enter> ocurre cuando el cursor entra al botón: cambia el color, pero solo si el botón está activo.
  # Lambda es una función pequeña sin nombre, la usamos porque bind necesita una función.
  # La "e" es el evento del mouse, que recibe lambda aunque no la usemos.
  boton.bind("<Enter>", lambda e: boton.config(bg=hover) if str(boton["state"]) == "normal" else None)

  # <Leave> ocurre cuando el mouse sale del botón: vuelve a su color original
  boton.bind("<Leave>", lambda e: boton.config(bg=fondo))

def crearBoton(contenedor: tk.Frame, texto: str, fondo: str, colorTexto: str, hover: str) -> tk.Button:
  """
    Crear un botón con estilo y colocarlo en la barra.

    Parameters:

      contenedor(tk.Frame): Donde se pondrá el botón.
      texto(str): Texto del botón.
      fondo(str): Color de fondo.
      colorTexto(str): Color de la letra.
      hover(str): Color al pasar el ratón.

    Returns:

      tk.Button: El botón (todavía sin acción asignada).
  """
  boton = tk.Button(contenedor, text=texto)
  estilizarBoton(boton, fondo, colorTexto, hover)
  activarHover(boton, fondo, hover)
  boton.pack(side="left", padx=12)
  return boton

def crearBotones(contenedor: tk.Frame) -> dict:
  """
    Crear los tres botones del juego.

    Parameters:

      contenedor(tk.Frame): Barra donde se colocarán.

    Returns:

      dict: Botones con las claves "pedir", "plantarse" y "nueva".
  """
  botones = {"pedir": crearBoton(contenedor, "Pedir carta", DORADO, "#1b1b1b", DORADO_CLARO), "plantarse": crearBoton(contenedor, "Plantarse", BORDO, CREMA, BORDO_CLARO), "nueva": crearBoton(contenedor, "Nueva partida", "#0e5a33", DORADO_CLARO, "#13744a")}
  return botones

def ejecutarVentana(ventana: tk.Tk) -> None:
  """
    Mantener la ventana abierta esperando las acciones del usuario.

    Parameters:

      ventana(tk.Tk): Ventana a ejecutar.

    Returns:

      None: No termina hasta que se cierra la ventana.
  """
  ventana.mainloop()
