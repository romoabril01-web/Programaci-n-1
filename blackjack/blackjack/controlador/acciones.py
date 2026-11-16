"""
Acciones del juego: lo que pasa cuando el usuario presiona un botón.

Aquí se unen la lógica y la interfaz: cada acción le pide cosas a la
lógica (logica/) y después actualiza lo que se ve (interfaz/).

Biblioteca usada: tkinter (temporizadores con after y botones con config).
"""

from logica.juego import (iniciarPartida, esTurnoJugador, jugadorPideCarta, jugadorSePaso, pasarTurnoAlDealer, dealerDebePedir, dealerPideCarta, calcularResultado, terminarPartida)
from controlador.contexto import refrescar, cancelarTemporizador

def turnoDealer(contexto: dict) -> None:
  """
    Hacer que el dealer pida una carta, o termine si ya tiene 17 o más.

    Parameters:

      contexto(dict): Contexto del programa.

    Returns:

      None: Se vuelve a llamar sola cada 0.8 segundos hasta que el dealer termine.
  """
  juego = contexto["juego"]

  if dealerDebePedir(juego):
    dealerPideCarta(juego)
    refrescar(contexto)
    # Después de repartir una carta, esperamos 800 milisegundos y volvemos a llamar a turnoDealer. Se repite hasta que el dealer llegue a 17 o más puntos.
    contexto["temporizador"] = contexto["ventana"].after(800, turnoDealer, contexto)
  else:
    # Ya no hay temporizador pendiente porque el dealer terminó de jugar
    contexto["temporizador"] = None
    terminarPartida(juego, calcularResultado(juego))
    refrescar(contexto)

def alPedirCarta(contexto: dict) -> None:
  """
    Acción del botón "Pedir carta".

    Parameters:

      contexto(dict): Contexto del programa.

    Returns:

      None: Reparte una carta al jugador y termina la partida si se pasó.
  """
  juego = contexto["juego"]

  # Si no es el turno del jugador, el botón no hace nada
  if not esTurnoJugador(juego):
    return

  jugadorPideCarta(juego)

  if jugadorSePaso(juego):
    terminarPartida(juego, calcularResultado(juego))

  refrescar(contexto)


def alPlantarse(contexto: dict) -> None:
  """
    Acción del botón "Plantarse".

    Parameters:

      contexto(dict): Contexto del programa.

    Returns:

      None: Pasa el turno al dealer y programa su jugada.
  """
  juego = contexto["juego"]

  # Si no es el turno del jugador, el botón no hace nada
  if not esTurnoJugador(juego):
    return

  pasarTurnoAlDealer(juego)
  refrescar(contexto)
  # after(700, turnoDealer, contexto) le dice a tkinter: "espera 700 milisegundos y luego ejecuta turnoDealer(contexto)". Así el dealer no juega de golpe y se alcanza a ver.
  # Guardamos el resultado en "temporizador" para poder cancelarlo después si hace falta.
  contexto["temporizador"] = contexto["ventana"].after(700, turnoDealer, contexto)

def alNuevaPartida(contexto: dict) -> None:
  """
    Acción del botón "Nueva partida".

    Parameters:

      contexto(dict): Contexto del programa.

    Returns:

      None: Cancela cualquier turno pendiente y reparte de nuevo.
  """
  cancelarTemporizador(contexto)
  iniciarPartida(contexto["juego"])
  refrescar(contexto)


def conectarBotones(contexto: dict) -> None:
  """
    Asignar a cada botón la acción que le corresponde.

    Parameters:

      contexto(dict): Contexto del programa.

    Returns:

      None: Configura el command de los tres botones.
  """
  # command necesita una función sin argumentos; lambda la crea para poder pasar el contexto
  contexto["botones"]["pedir"].config(command=lambda: alPedirCarta(contexto))
  contexto["botones"]["plantarse"].config(command=lambda: alPlantarse(contexto))
  contexto["botones"]["nueva"].config(command=lambda: alNuevaPartida(contexto))
