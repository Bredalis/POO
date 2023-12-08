
"""
El polimorfismo se refiere a 
la capacidad de diferentes 
objetos de responder a una 
misma acción o mensaje de 
maneras diferentes. Permite 
tratar objetos de diferentes 
clases de manera uniforme a 
través de una interfaz común, 
lo que simplifica el diseño y 
promueve la reutilización de 
código. Puede ser estático 
(sobrecarga de métodos) o 
dinámico (sobrescritura de métodos).
"""

"""
Programa que muestra el sueldo 
de diferentes empleados
"""

class Empleado:

	def __init__(self, nombre, sueldo_mensual):

		# Propiedades

		self.nombre = nombre
		self.sueldo_mensual = sueldo_mensual

	# Funcion que calcula el sueldo anual de un empleado

	def Calcular(self):
		sueldo = 12*self.sueldo_mensual*(1 + 1/100)
		print(f"El sueldo anual de {self.nombre}, empleado normal, es de {sueldo}")

class Contable(Empleado):

	# Hereda las propiedades de la clase Empleados

	def __init__(self, nombre, sueldo_mensual):
		super().__init__(nombre, sueldo_mensual)

	# Funcion que calcula el sueldo anual de un contable

	def Calcular(self):
		sueldo = 12*self.sueldo_mensual*(1 + 4/100)
		print(f"El sueldo anual de {self.nombre}, contable, es de {sueldo}")

class Publicista(Empleado):

	# Hereda las propiedades de la clase Empleado

	def __init__(self, nombre, sueldo_mensual):
		super().__init__(nombre, sueldo_mensual)

	# Funcion que calcula el sueldo anual de un publicista

	def Calcular(self):
		sueldo = 12*self.sueldo_mensual*(1 + 5/100)
		print(f"El sueldo anual de {self.nombre}, publicista, es de {sueldo}")

empleados = [
	Empleado("Juan", 1000),
	Contable("Juana", 2000),
	Publicista("Lucas", 1200)
]

for empleado in empleados:
	empleado.Calcular()