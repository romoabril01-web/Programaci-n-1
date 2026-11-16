"""
Constantes del aspecto visual: tamaños, fuentes, colores y mensajes.

Biblioteca usada: tkinter. Los colores se escriben como texto "#rrggbb" y las fuentes como tuplas (nombre, tamaño, estilo).
"""

# Tamaños
ANCHO = 820
ALTO_MESA = 620
CARTA_W = 90
CARTA_H = 130

# Tipografías
FUENTE_TITULO = "Georgia"
FUENTE_TEXTO = "Segoe UI"

# Paleta: verde casino + dorado + burdeos + crema
COLOR_FONDO = "#094527"
COLOR_FONDO_BARRA = "#04251a"
COLOR_FONDO_MENSAJE = "#06301c"
DORADO = "#d4af37"
DORADO_CLARO = "#f1d570"
DORADO_OSCURO = "#8f7a2a"
CREMA = "#fffdf5"
BORDE_CARTA = "#b8a97a"
BORDO = "#7b1e3a"
BORDO_CLARO = "#9b2c4d"
CARTA_NEGRA = "#1f1f1f"
CARTA_ROJA = "#c62828"
PALO_ROJO_TITULO = "#e57060"
SOMBRA_TITULO = "#03200f"
COLOR_TEXTO = "#f5f0dc"
COLOR_VERDE = "#7cffb2"
COLOR_ROJO = "#ff8a80"
COLOR_AMARILLO = "#ffd54f"

# Mensaje y color que se muestran para cada estado del juego
MENSAJES = {
    "sin_iniciar": ("", COLOR_TEXTO),
    "turno_jugador": ("Tu turno: pide una carta o plántate", COLOR_TEXTO),
    "turno_dealer": ("Turno del dealer...", COLOR_TEXTO),
    "jugador_blackjack": ("¡BlackJack natural! Ganas la partida.", COLOR_VERDE),
    "dealer_blackjack": ("El dealer tiene BlackJack natural. Gana el dealer.", COLOR_ROJO),
    "empate_blackjack": ("¡Empate! Ambos tienen BlackJack natural.", COLOR_AMARILLO),
    "jugador_pasa": ("Te pasaste de 21. Gana el dealer.", COLOR_ROJO),
    "dealer_pasa": ("El dealer se pasó de 21. ¡Ganas!", COLOR_VERDE),
    "jugador_gana": ("¡Ganas! Tienes más puntos que el dealer.", COLOR_VERDE),
    "dealer_gana": ("Gana el dealer. Tiene más puntos.", COLOR_ROJO),
    "empate": ("¡Empate! Misma puntuación.", COLOR_AMARILLO),
}
