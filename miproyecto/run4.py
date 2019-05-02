"""
	file run4.py
	autor: Andres Vallejo

	Deseamos obtener el costo de una carrera universitaria.
	El valor promedio de cada ciclo es de 1200$.

	El valor promedio del seguro educativo es de 100$.
		Si la edad del estudiante es menor o igual a 20
			Caso contrario sera de 150$
	Si el estuduiante tiene una modalidad a distacia el numero de ciclos a seguir es de 10.
		caso contrario debera seguir 8 ciclos

		obtenerbtener la proyeccion del costo de la carrera de un estudiante.	
"""

c = int (1200) # Valor ciclo promedio
edad = input ("ingrese la edad: ")
edad = int (edad) # Edad del estudiante
modalidad = input("Ingrese la modalidad: ") #Ingreso de la Modalidad
# Condicional
if (edad<=20) and (modalidad == "Distancia"): # Comparacion edad y modalidad
	seguro = 100
	ciclos = 10
else:
	seguro = 150
	ciclos = 8
# S = Ek valor completo del Seguro Educativo
S =  (seguro * ciclos)
M =  (c * ciclos)
#Matricual = El costo totaol 
Matricula = int (S + M)	# Sumatoria total del ciclo más el Seguro

 
print ("%s  - El valor total   %d"  % ("Matricula", Matricula)) 