//Nombre del archivo: imcAdulto.psc
//Descripcion: algoritmo que calcule el índice de masa corporal (IMC) de una persona adulta de al menos 20 años e indique la categoría de peso en la que se encuentra.
//Nombres: Chen Huiru, Romo Morales Abril Yaneth 
//Fecha: 28/08/26

//Las categorías de IMC para adultos son las siguientes:

//Bajo peso severo: IMC por debajo de 16.5
//Bajo peso: IMC desde 16.5 y por debajo de 18.5
//Peso saludable: IMC desde 18.5 y por debajo de 25.0
//Sobrepeso: IMC desde 25.0 y por debajo de 30.0
//Obesidad tipo I (moderada): IMC desde 30.0 y por debajo de 35.0
//Obesidad tipo  II (severa): IMC desde 35.0 y por debajo de 40.0
//Obesidad tipo III (mórbida): IMC de 40.0 o más

Proceso imcAdulto
	
	Escribir "Calculadora de IMC"
	Definir edad, altura, peso, IMC Como Real
	
	Escribir "Indica tu edad en años " Sin Saltar 
	Leer edad
	
	//Si la edad es menor que 20 entonces el algoritmo invalida los datos
	Si edad < 20 Entonces
		Escribir "Datos invalidos"
	FinSi
	
	//Si la edad es mayor o igual a 20 entonces continua el proceso
	Si edad >= 20 Entonces
		Escribir "Datos validos"
		
		Escribir Sin Saltar "Indica tu altura en metros "
		Leer altura
		
		Escribir Sin Saltar "Introduce tu peso en kg "
		Leer peso
		
		//El IMC se calcula con la fórmula:
		imc <- peso/(altura*altura) 
		
		//Indicar el imc
		Escribir "Tu IMC es: ", imc
		
		
		//Indicar la categoria de peso
		Si imc < 16.5 Entonces
			Escribir "Categoria de peso: Bajo peso severo"
		FinSi
		
		Si imc >= 16.5 Y imc < 18.5 Entonces
			Escribir "Categoria de peso: Bajo peso"
		FinSi
		
		Si imc >= 18.5 Y imc < 25.0 Entonces
			Escribir "Categoria de peso: Peso saludable"
		FinSi
		
		Si imc >= 25.0 Y imc < 30 Entonces 
			Escribir "Categoria de peso: Sobrepeso"
		FinSi
		
		Si imc >= 30 Y imc < 35 Entonces
			Escribir "Categoria de peso: Obesidad tipo l (moderada)"
		FinSi
		
		Si imc >= 35 Y imc < 40 entonces 
			Escribir "Categoria de peso: Obesidad tipo ll (severa)"
		FinSi
		
		Si imc >= 40 Y imc < 45 Entonces 
			Escribir "Categoria de peso: Obesidad tipo lll (mórbida)"
		FinSi
	FinSi
	
	
FinProceso
	
	