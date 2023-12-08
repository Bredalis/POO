
"""
Programa que murestra 
el numero PI y calcula 
el perimetro, radio y 
area de un circulo
"""

class Circulo:

	def __init__(self, radio):

		# Propiedades

		self.__radio = radio
		self.__pi = 3.1415

	def Calcular_Perimetro(self):
		print(f"Perimetro: {2*self.__pi*self.__radio}")

	def Calcular_Area(self):
		print(f"Area: {self.__pi*self.__radio**2}")

	def Obtener_PI(self):
		print(f"PI: {self.__pi}")

	def Obtener_Radio(self, valor):

		# Si el valor no es positivo no se mostrara el radio

		if type(valor) == int or type(valor) == float:

			if valor > 0:
				self.__radio = valor
				print(f"Radio: {self.__radio}")

			else:
				print("No puede ser negativo")

		else:
			print("Tiene que ser un numero positivo")

"""
Muestra del perimetro, 
area, radio y PI de un circulo
"""

print("Propiedades de un circulo:\n")

circulo = Circulo(2.5)

circulo.Calcular_Perimetro()
circulo.Calcular_Area()

circulo.Obtener_PI()
circulo.Obtener_Radio(1)