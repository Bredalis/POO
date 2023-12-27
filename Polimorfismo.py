
"""
Programa que muestra el sueldo 
de diferentes empleados
"""

class empleado:
	def __init__(self, nombre, sueldo_mensual):

		# Propiedades

		self.nombre = nombre
		self.sueldo_mensual = sueldo_mensual

	# Funcion que calcula el sueldo anual de un empleado

	def calcular(self):
		sueldo = 12 * self.sueldo_mensual * (1 + 1 / 100)
		print(f'El sueldo anual de {self.nombre}, empleado, es de {sueldo}')

class contable(empleado):

	# Hereda las propiedades de la clase Empleados

	def __init__(self, nombre, sueldo_mensual):
		super().__init__(nombre, sueldo_mensual)

	# Funcion que calcula el sueldo anual de un contable

	def calcular(self):
		sueldo = 12 * self.sueldo_mensual * (1 + 4 / 100)
		print(f'El sueldo anual de {self.nombre}, contable, es de {sueldo}')

class publicista(empleado):

	# Hereda las propiedades de la clase empleado

	def __init__(self, nombre, sueldo_mensual):
		super().__init__(nombre, sueldo_mensual)

	# Funcion que calcula el sueldo anual de un publicista

	def calcular(self):
		sueldo = 12 * self.sueldo_mensual * (1 + 5 / 100)
		print(f'El sueldo anual de {self.nombre}, publicista, es de {sueldo}')

empleados = [
	empleado('Juan', 1000),
	contable('Juana', 2000),
	publicista('Lucas', 1200)
]

for empleado in empleados:
	empleado.calcular()