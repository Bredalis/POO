
"""
Programa que murestra 
el numero PI y calcula 
el perimetro, radio y 
area de un circulo
"""

class circulo:
	def __init__(self, radio):

		# Propiedades

		self.__radio = radio
		self.__pi = 3.1415

	def calcular_perimetro(self):
		print(f'Perimetro: {2 * self.__pi*self.__radio}')

	def calcular_area(self):
		print(f'Area: {self.__pi * self.__radio ** 2}')

	def obtener_pi(self):
		print(f'PI: {self.__pi}')

	def obtener_radio(self, valor):

		# Si el valor no es positivo no se mostrara el radio

		if type(valor) == int or type(valor) == float:

			if valor > 0:
				self.__radio = valor
				print(f'Radio: {self.__radio}')

			else:
				print('No puede ser negativo')
		else:
			print('Tiene que ser un numero positivo')

"""
Muestra del perimetro, 
area, radio y PI de un circulo
"""

print('Propiedades de un circulo:\n')

circulo = circulo(2.5)

circulo.calcular_perimetro()
circulo.calcular_area()

circulo.obtener_pi()
circulo.obtener_radio(1)