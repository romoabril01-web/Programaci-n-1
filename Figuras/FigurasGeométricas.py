# Archivo: FigurasGeométricas.py
# Descripción: Programa en Python que imprime las siguientes figuras rellenas y huecas: un reloj de arena, un rombo, un moño y una copa.
# Autor: Chen Huiru, Romo Morales Abril Yaneth
# Fecha: 03/11/2026

def Figuras(opcion:int , tamaño : int , simbolo:str , tipo: int) -> None:
    """
    Imprimir figuras geométricas rellenas o huecas.
    
    Parameters:
        
        opcion(int): Figura que se desea imprimir u opción para salir.
            1: Reloj de arena
            2: Rombo
            3: Moño
            4: Copa
            5: Todas las figuras
            6: Salir
                
        tamaño(int): Dimensión impar entre 5 y 21.
        
        simbolo (str): Carácter utilizado para dibujar las figuras.

        tipo (int): Tipo de figura.
            1: Rellena
            2: Hueca
            
        Returns:
        
            None: Imprime las figuras en pantalla.
            
        Raises:
        
            TypeError: Si los argumentos tienen tipos incorrectos.
            ValueError: Si la opción, dimensión, símbolo o tipo de figura no son válidos.
    """

    if not isinstance (opcion, int):
        raise TypeError("La opción debe ser un número entero.")
    
    if opcion not in range(1, 6):
        raise ValueError("La opción debe estar entre 1 y 5")
    
    if not isinstance (tamaño, int):
        raise TypeError("La dimensión debe ser un número entero.")
    
    if tamaño < 5 or tamaño > 21 or tamaño % 2 == 0:
        raise ValueError("La dimensión debe ser un número impar entre 5 y 21, incluidos.")
    
    if not isinstance (simbolo, str):
        raise TypeError("El símbolo debe ser una cadena")
    
    if len(simbolo)!= 1 or simbolo.isspace():
        raise TypeError("Debe ingresar un solo símbolo válido(ejemplo:*./)")
    
    if not isinstance (tipo, int):
        raise TypeError("El tipo debe ser un número entero.")
    
    if tipo not in range(1,3):
        raise ValueError("El tipo debe ser 1 (rellena) o 2 (hueca)")
    
    mitad = tamaño // 2
    nombres = ["", "RELOJ DE ARENA", "ROMBO"]
    
    print("\n" + nombres[opcion])

    total = tamaño 

    for i in range(total):
        match opcion:
            # Reloj de arena
            case 1:
                espacios = min(i, tamaño - 1 - i)
                ancho = tamaño - 2 * espacios
            # Rombo
            case 2:
                espacios = abs(mitad - i)
                ancho = tamaño - 2 * espacios

        # Rellena / Hueca
        if tipo == 1:
            linea = simbolo * ancho
        else:
            linea = simbolo if ancho == 1 else simbolo + " " * (ancho - 2) + simbolo

        print(" " * espacios + linea)

print("Programa que imprime figuras rellenas y huecas, según la dimensión que el usuario desee.")

while True:
    print("\n===== MENÚ DE FIGURAS =====")
    print("1. Reloj de arena")
    print("2. Rombo")
    print("3. Moño")
    print("4. Copa")
    print("5. Todas las figuras")
    print("6. Salir")

    try:
        opcion = int(input("Seleccione una opción: "))

        match opcion:
            case 1 | 2 | 3 | 4 | 5 :
                tamaño = int(input("Dimensión impar (5-21): "))
                simbolo = input("Símbolo: ")
                tipo = int(input("Tipo 1. Rellena 2. Hueca: "))
                Figuras(opcion, tamaño, simbolo, tipo)
            case 6:
                print("Gracias por utilizar este programa.")
                break
            case _:
                print("Opción inválida")

    except (ValueError, TypeError) as e:
        print("Error:", e)