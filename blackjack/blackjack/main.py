"""
Tarea 5. 21: BlackJack
Descripción:
    Juego de BlackJack de un jugador contra el dealer (sin apuestas).
    El jugador puede pedir carta o plantarse; después juega el dealer,
    que está obligado a pedir cartas mientras tenga menos de 17 puntos.
Autor: Huiru Chen, Abril Yaneth Romo Morales
Fecha: 11/11/2026

Bibliotecas usadas:
    - tkinter: biblioteca gráfica de Python. Con ella se crea la ventana,
      el canvas donde se dibujan la mesa y las cartas (rectángulos, texto,
      líneas) y los botones. Solo se usa dentro de las carpetas
      interfaz/ y controlador/.
    - random: se usa en logica/mazo.py para mezclar el mazo.

Estructura del proyecto:
    main.py          -> proceso principal: solo llama a funciones de las carpetas.
    logica/          -> reglas del juego (mazo, puntos, estado). Sin nada visual.
    interfaz/        -> todo lo que se dibuja (ventana, mesa, cartas, botones).
    controlador/     -> acciones de los botones: unen la lógica con la interfaz.

Cómo ejecutarlo:
    Abrir main.py y ejecutarlo (en Thonny: botón verde o F5).
    Debe estar en la misma carpeta que logica/, interfaz/ y controlador/.
"""

from logica.juego import crearJuego
from interfaz.ventana import (crearVentana, crearCanvas, crearBarraBotones, crearBotones, ejecutarVentana)
from controlador.contexto import crearContexto
from controlador.acciones import conectarBotones, alNuevaPartida

def main() -> None:
  """
    Armar el juego, empezar la primera partida y abrir la ventana.

    Returns:

      None: No termina hasta que se cierra la ventana.
  """
  ventana = crearVentana()
  canvas = crearCanvas(ventana)
  contenedor = crearBarraBotones(ventana)
  botones = crearBotones(contenedor)

  juego = crearJuego()
  contexto = crearContexto(ventana, canvas, juego, botones)

  conectarBotones(contexto)
  alNuevaPartida(contexto)

  ejecutarVentana(ventana)


if __name__ == "__main__":
  main()
