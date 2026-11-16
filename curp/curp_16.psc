// Titulo: curp_16.psc
// Descripción: Algoritmo que captura la información del user y genera los 16 caracteres de la curp
// Autores: Huiru Chen, Abril Yaneth Romo Morales
// Fecha: 11/10/2026
Proceso curp_16
	Escribir "Algoritmo que genera 16 caracteres de la curp"
	
	Definir nombre, paterno, materno, s, entidad Como Caracter
	Definir dia, mes, anio Como Entero
	
	// Función 1
	Escribir "Escribe los datos tal como aparecen en tu acta de nacimiento."
	Escribir Sin Saltar "Nombre(s): "
	Leer nombre
	Escribir Sin Saltar "Primer apellido: "
	Leer paterno
	Escribir Sin Saltar "Segundo apellido (deja vacio si no tienes): "
	Leer materno
	
	// Función 2
	Escribir Sin Saltar "Día de nacimiento (1-31): "
	Leer dia
	Escribir Sin Saltar "Mes de nacimiento (1-12): "
	Leer mes
	Escribir Sin Saltar "Año de nacimiento (<=2026): "
	Leer anio
	
	// Sin función
	Repetir
		Escribir Sin Saltar "Sexo M (mujer), H (Hombre): "
		Leer s
		// Convertimos a mayúsculas por si el usuario escribe minúscula (m o h)
		s <- Mayusculas(s)
		
		Si s <> "M" Y s <> "H" Entonces
			Escribir "Opción inválida. Por favor, escribe M o H."
		FinSi
	Hasta Que s = "M" O s = "H"
	
	//Función 3
    Escribir Sin Saltar "Ingrese su entidad federativa de nacimiento: "
    Leer entidad
	
	Escribir "Clave CURP: ", caracter1a4(nombre, paterno, materno), caracter5a10(dia, mes, anio), Mayusculas(s), caracter12a13(entidad), caracter14a16(nombre, paterno, materno)
FinProceso

Funcion resultado <- caracter1a4(nombre, paterno, materno)
	Definir resultado, txt, c, conAcento, sinAcento, alfabeto, actual, palabra, elegida, respaldo, letraIni, vocal, lista, l1, l2, l3, l4 Como Caracter
	Definir campo, i, j, k, cuenta, base Como Entero
	Definir esNombre, saltaPrimera, encontrada, esLetra, terminado Como Logico
	
	// Detecta si la subcadena cuenta desde 0 (base = 0) o desde 1 (base = 1)
	Si Subcadena("AB", 1, 1) = "B" Entonces
		base <- 0
	SiNo
		base <- 1
	FinSi
	
	conAcento <- "áéíóúÁÉÍÓÚüÜñ"
	sinAcento <- "AEIOUAEIOUUUÑ"
	alfabeto <- "ABCDEFGHIJKLMNOPQRSTUVWXYZÑ"
	
	l1 <- "X"
	l2 <- "X"
	l3 <- "X"
	l4 <- "X"
	
	// campo 1 = nombre, campo 2 = primer apellido, campo 3 = segundo apellido
	Para campo <- 1 Hasta 3 Con Paso 1 Hacer
		// Tomar el texto del campo
		Si campo = 1 Entonces
			txt <- nombre
		FinSi
		Si campo = 2 Entonces
			txt <- paterno
		FinSi
		Si campo = 3 Entonces
			txt <- materno
		FinSi
		esNombre <- (campo = 1)
		
		// Limpiar: mayusculas, sin acentos ni dieresis 
		actual <- ""
		Para i <- 1 Hasta Longitud(txt) Con Paso 1 Hacer
			c <- Subcadena(txt, i - 1 + base, i - 1 + base)
			Para j <- 1 Hasta Longitud(conAcento) Hacer
				Si c = Subcadena(conAcento, j - 1 + base, j - 1 + base) Entonces
					c <- Subcadena(sinAcento, j - 1 + base, j - 1 + base)
				FinSi
			FinPara
			actual <- Concatenar(actual, c)
		FinPara
		txt <- Concatenar(Mayusculas(actual), " ")
		
		// Elegir la palabra que cuenta
		// En nombres compuestos se salta Maria, Jose (J, Ma, Ma., J.)
		// Se salta (DE, LA, LOS, MC, VON, ...)
		actual <- ""
		cuenta <- 0
		elegida <- ""
		respaldo <- ""
		encontrada <- Falso
		saltaPrimera <- Falso
		Para i <- 1 Hasta Longitud(txt) Con Paso 1 Hacer
			c <- Subcadena(txt, i - 1 + base, i - 1 + base)
			Si c <> " " Entonces
				actual <- Concatenar(actual, c)
			SiNo
				Si actual <> "" Entonces
					cuenta <- cuenta + 1
					Si cuenta = 1 Entonces
						respaldo <- actual
						Si esNombre Y (actual = "MARIA" O actual = "MA" O actual = "MA." O actual = "JOSE" O actual = "J" O actual = "J.") Entonces
							saltaPrimera <- Verdadero
						FinSi
					FinSi
					Si cuenta = 2 Y saltaPrimera Entonces
						respaldo <- actual
					FinSi
					Si No encontrada Y No (cuenta = 1 Y saltaPrimera) Entonces
						Si No (actual = "DA" O actual = "DAS" O actual = "DE" O actual = "DEL" O actual = "DER" O actual = "DI" O actual = "DIE" O actual = "DD" O actual = "EL" O actual = "LA" O actual = "LOS" O actual = "LAS" O actual = "LE" O actual = "LES" O actual = "MAC" O actual = "MC" O actual = "VAN" O actual = "VON" O actual = "Y") Entonces
							elegida <- actual
							encontrada <- Verdadero
						FinSi
					FinSi
					actual <- ""
				FinSi
			FinSi
		FinPara
		Si encontrada Entonces
			palabra <- elegida
		SiNo
			palabra <- respaldo
		FinSi
		
		// Letra inicial y primera vocal interna
		// Ñ o caracter especial (/ - .) -> X, sin vocal interna -> X
		letraIni <- "X"
		vocal <- "X"
		Si palabra <> "" Entonces
			c <- Subcadena(palabra, base, base)
			esLetra <- Falso
			Para k <- 1 Hasta 26 Con Paso 1 Hacer
				Si c = Subcadena(alfabeto, k - 1 + base, k - 1 + base) Entonces
					esLetra <- Verdadero
				FinSi
			FinPara
			Si esLetra Entonces
				letraIni <- c
			FinSi
			
			i <- 2
			terminado <- Falso
			Mientras i <= Longitud(palabra) Y No terminado Hacer
				c <- Subcadena(palabra, i - 1 + base, i - 1 + base)
				Si c = "A" O c = "E" O c = "I" O c = "O" O c = "U" Entonces
					vocal <- c
					terminado <- Verdadero
				SiNo
					esLetra <- Falso
					Para k <- 1 Hasta 27 Con Paso 1 Hacer
						Si c = Subcadena(alfabeto, k - 1 + base, k - 1 + base) Entonces
							esLetra <- Verdadero
						FinSi
					FinPara
					Si No esLetra Entonces
						vocal <- "X"
						terminado <- Verdadero
					FinSi
				FinSi
				i <- i + 1
			FinMientras
		FinSi
		
		// Guardar segun el campo 
		Si campo = 1 Entonces
			l4 <- letraIni
		FinSi
		Si campo = 2 Entonces
			l1 <- letraIni
			l2 <- vocal
		FinSi
		Si campo = 3 Entonces
			l3 <- letraIni
		FinSi
	FinPara
	
	// Armar las 4 letras
	resultado <- Concatenar(Concatenar(l1, l2), Concatenar(l3, l4))
	
	// Palabras inconvenientes: 2a letra -> X 
	lista <- "BACABAKABUEIBUEYCACACACOCAGACAGOCAKACAKOCOGECOGICOJACOJECOJICOJOCOLACULOFALOFETOGETAGUEIGUEYJETAJOTOKACAKACOKAGAKAGOKAKAKAKOKOGEKOGIKOJAKOJEKOJIKOJOKOLAKULOLILOLOCALOCOLOKALOKOMAMEMAMOMEARMEASMEONMIARMIONMOCOMOKOMULAMULONACANACOPEDAPEDOPENEPIPIPITOPOPOPUTAPUTOQULORATAROBAROBEROBORUINSENOTETAVACAVAGAVAGOVAKAVUEIVUEYWUEIWUEY"
	Para i <- 0 Hasta 80 Con Paso 1 Hacer
		Si resultado = Subcadena(lista, i * 4 + base, i * 4 + 3 + base) Entonces
			resultado <- Concatenar(Concatenar(l1, "X"), Concatenar(l3, l4))
		FinSi
	FinPara
FinFuncion

Funcion FechaYAnio <- caracter5a10(dia , mes , anio)
	Definir FechaYAnio Como Caracter
	Definir numAnio , numMes , numDia Como Caracteres
	
	Si dia < 10 Entonces 
		numDia <- Concatenar("0" , ConvertirATexto(dia))
	SiNo 
		numDia <- ConvertirATexto(dia)
	FinSi
	
	Si mes < 10 Entonces 
		numMes <- Concatenar("0" , ConvertirATexto(mes))
	SiNo 
		numMes <- ConvertirATexto(mes)
	FinSi
	
	anio <- anio MOD 100
	
	Si anio < 10 Entonces 
		numAnio <- Concatenar("0" , ConvertirATexto(anio))
	SiNo 
		numAnio <- ConvertirATexto(anio)
	FinSi
	
	FechaYAnio <- Concatenar ( Concatenar(numAnio, numMes) , numDia)
FinFuncion

Funcion clave <- caracter12a13(entidad)
	Definir clave Como Cadena
	
	Segun Mayusculas(entidad) Hacer
        "AGUASCALIENTES":
            clave <- "AS"
        "BAJA CALIFORNIA":
            clave <- "BC"
        "BAJA CALIFORNIA SUR":
            clave <- "BS"
        "CAMPECHE":
            clave <- "CC"
        "COAHUILA":
            clave <- "CL"
        "COLIMA":
            clave <- "CM"
        "CHIAPAS":
            clave <- "CS"
        "CHIHUAHUA":
            clave <- "CH"
        "CIUDAD DE MEXICO":
            clave <- "DF"
        "DURANGO":
            clave <- "DG"
        "GUANAJUATO":
            clave <- "GT"
        "GUERRERO":
            clave <- "GR"
        "HIDALGO":
            clave <- "HG"
        "JALISCO":
            clave <- "JC"
        "MEXICO":
            clave <- "MC"
        "MICHOACAN":
            clave <- "MN"
        "MORELOS":
            clave <- "MS"
        "NAYARIT":
            clave <- "NT"
        "NUEVO LEON":
            clave <- "NL"
        "OAXACA":
            clave <- "OC"
        "PUEBLA":
            clave <- "PL"
        "QUERETARO":
            clave <- "QT"
        "QUINTANA ROO":
            clave <- "QR"
        "SAN LUIS POTOSI":
            clave <- "SP"
        "SINALOA":
            clave <- "SL"
        "SONORA":
            clave <- "SR"
        "TABASCO":
            clave <- "TC"
        "TAMAULIPAS":
            clave <- "TS"
        "TLAXCALA":
            clave <- "TL"
        "VERACRUZ":
            clave <- "VZ"
        "YUCATAN":
            clave <- "YN"
        "ZACATECAS":
            clave <- "ZS"
        "NACIDO EN EL EXTRANJERO":
            clave <- "NE"
        De Otro Modo:
			Escribir "Error"
    FinSegun
FinFuncion

Funcion consonantes <- caracter14a16(nombre, paterno, materno)
	Definir c14, c15, c16, consonantes, letra, nomLimpio Como Caracter
	Definir i Como Entero
	Definir encontrada Como Logico
	
	// Convertir a mayúsculas 
	nombre <- Mayusculas(nombre)
	paterno <- Mayusculas(paterno)
	materno <- Mayusculas(materno)
	
	//xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
	// Posición 14: Primera consonante interna del apellido paterno
	c14 <- "X"
	encontrada <- Falso
	i <- 2
	Mientras i <= Longitud(paterno) Y No encontrada Hacer
		letra <- Subcadena(paterno, i, i)
		Si letra = "Ñ" Entonces
			// La Ñ se remplaza como X
			c14 <- "X" 
			encontrada <- Verdadero
		SiNo
			// Si no es vocal ni espacio ni caracter especial, es consonante
			Si letra <> "A" Y letra <> "E" Y letra <> "I" Y letra <> "O" Y letra <> "U" Y letra >= "A" Y letra <= "Z" Entonces
				c14 <- letra
				encontrada <- Verdadero
			FinSi
		FinSi
		i <- i + 1
	FinMientras
	
	// xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
	// Posición 15: Primera consonante interna del apellido materno
	c15 <- "X"
	Si Longitud(materno) > 0 Entonces
		encontrada <- Falso
		i <- 2
		Mientras i <= Longitud(materno) Y No encontrada Hacer
			letra <- Subcadena(materno, i, i)
			Si letra = "Ñ" Entonces
				c15 <- "X"
				encontrada <- Verdadero
			SiNo
				Si letra <> "A" Y letra <> "E" Y letra <> "I" Y letra <> "O" Y letra <> "U" Y letra >= "A" Y letra <= "Z" Entonces
					c15 <- letra
					encontrada <- Verdadero
				FinSi
			FinSi
			i <- i + 1
		FinMientras
	Sino
		// Si solo tiene un apellido, la posición 15 es X
		c15 <- "X" 
	FinSi
	
	// xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
	// Posición 16: Primera consonante interna del nombre
	nomLimpio <- nombre
	
	// Si el nombre empieza con MARIA o JOSE, nos saltamos el primer nombre
	Si Subcadena(nombre, 1, 6) = "MARIA " O Subcadena(nombre, 1, 3) = "MA. " O Subcadena(nombre, 1, 3) = "MA " Entonces
		nomLimpio <- Subcadena(nombre, 7, Longitud(nombre))
	FinSi
	Si Subcadena(nombre, 1, 5) = "JOSE " O Subcadena(nombre, 1, 2) = "J. " O Subcadena(nombre, 1, 2) = "J " Entonces
		nomLimpio <- Subcadena(nombre, 6, Longitud(nombre))
	FinSi
	
	c16 <- "X"
	encontrada <- Falso
	i <- 2
	Mientras i <= Longitud(nomLimpio) Y No encontrada Hacer
		letra <- Subcadena(nomLimpio, i, i)
		Si letra = "Ñ" Entonces
			c16 <- "X" 
			encontrada <- Verdadero
		SiNo
			Si letra <> "A" Y letra <> "E" Y letra <> "I" Y letra <> "O" Y letra <> "U" Y letra >= "A" Y letra <= "Z" Entonces
				c16 <- letra
				encontrada <- Verdadero
			FinSi
		FinSi
		i <- i + 1
	FinMientras
	
	// Unir los 3 caracteres finales
	consonantes <- Concatenar(Concatenar(c14, c15), c16)
FinFuncion
