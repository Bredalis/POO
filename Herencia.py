
"""
Uso de la Herencia de Jerarquia
en un ejemplo de ver el nombre, 
edad y dni de una persona y un trabajador
"""

class persona:
	def __init__(self, nombre, edad, dni):

		# Propiedades

		self.nombre = nombre
		self.edad = edad
		self.dni = dni

	# Mostrar informacion

	def presentarse(self):
		print(f'Nombre: {self.nombre} \nEdad: {self.edad}')

class trabajador(persona):

	# Hereda las propiedades de la clase persona
	
	def __init__(self, nombre, edad, dni, sueldo, cargo, empresa):
		super().__init__(nombre, edad, dni)

		self.sueldo = sueldo
		self.cargo = cargo
		self.empresa = empresa

	# Muestra el sueldo calculado

	def calcular_sueldo(self):
		print(f'Sueldo: {12 * self.sueldo + 2000}')

# Muestra los nombres, edades y dni

print('Informacion:\n')

oscar = persona('Oscar', 23, '76893434')
oscar.presentarse()

print('dni:', oscar.dni)

trabajador = trabajador(
	'Bredalis', 34, '564g98800', 21000, 'Programador', 'Google')

trabajador.presentarse()
trabajador.calcular_sueldo()