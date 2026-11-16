"""
Contexto del programa: junta en un solo diccionario todo lo que necesitan las acciones (ventana, canvas, juego, botones y temporizador).

Biblioteca usada: tkinter (solo a través de los objetos que recibe, por ejemplo configurar el estado de los botones con config).
"""

from interfaz.mesa import dibujarMesa
from logica.juego import esTurnoJugador

def crearContexto(ventana, canvas, juego: dict, botones: dict) -> dict:
  """
    Guardar en un solo diccionario todo lo que usan las acciones.

    Parameters:

      ventana(tk.Tk): Ventana principal.
      canvas(tk.Canvas): Área donde se dibuja la mesa.
      juego(dict): Diccionario del juego (lógica).
      botones(dict): Botones de la interfaz.

    Returns:

      dict: Contexto con las claves "ventana", "canvas", "juego", "botones" y "temporizador" (None mientras no haya ninguno esperando).
  """
  contexto = {
      "ventana": ventana,
      "canvas": canvas,
      "juego": juego,
      "botones": botones,
      "temporizador": None}
  return contexto

def actualizarPantalla(contexto: dict) -> None:
  """
    Volver a dibujar la mesa con el estado actual del juego.

    Parameters:

      contexto(dict): Contexto del programa.

    Returns:

      None: Actualiza el canvas.
  """
  dibujarMesa(contexto["canvas"], contexto["juego"])

def actualizarBotones(contexto: dict) -> None:
  """
    Activar o desactivar "Pedir carta" y "Plantarse" según el turno.

  Parameters:

      contexto(dict): Contexto del programa.

  Returns:

      None: Solo están activos durante el turno del jugador.
  """
  if esTurnoJugador(contexto["juego"]):
    estado = "normal"
  else:
    estado = "disabled"

  contexto["botones"]["pedir"].config(state=estado)
  contexto["botones"]["plantarse"].config(state=estado)


def refrescar(contexto: dict) -> None:
  """Actualizar todo lo que ve el usuario: la mesa y los botones.

    Parameters:

      contexto(dict): Contexto del programa.

    Returns:

      None: Actualiza pantalla y botones.
  """
  actualizarPantalla(contexto)
  actualizarBotones(contexto)


def cancelarTemporizador(contexto: dict) -> None:
  """
    Cancelar el temporizador del dealer si había uno esperando.

    Parameters:

      contexto(dict): Contexto del programa.

    Returns:

      None: Deja "temporizador" en None.
  """
  # Si el dealer estaba en medio de su turno y el jugador presiona "Nueva partida", hay un temporizador pendiente. after_cancel lo cancela para que el dealer de la partida anterior no siga repartiendo cartas en la partida nueva.
  # Si no hay temporizador pendiente, vale None y no se cancela nada.
  if contexto["temporizador"] is not None:
    contexto["ventana"].after_cancel(contexto["temporizador"])
    contexto["temporizador"] = None
