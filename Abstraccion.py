
"""
La abstracción se refiere a la 
simplificación de objetos complejos 
al enfocarse solo en los detalles 
relevantes para el problema en cuestión. 
"""

from abc import ABC, abstractmethod

class Personaje(ABC):

	@abstractmethod
	def __init__(self, nombre):

		self.nombre = nombre
		self.nivel = 0
		self.inventario = []
		self.vida = 100

	@abstractmethod
	def Atacar(self, objectivo):
		pass

	@abstractmethod
	def Estado(self):
		print(f"Nombre: {self.nombre} \nNivel: {self.nivel}")

	def Subir_nivel(self):
		self.nivel += 1

	def Obtener_inventario(self):
		print(f"Inventario de: {self.nombre}")

		for objecto in self.inventario:
			print(objecto)

class Mago(Personaje):

	def __init__(self, nombre):
		super().__init__(nombre)

		self.vida = 120
		self.inteligencia = 95
		self.inventario = ["Pocion de Mana", "Grimorio"]

	def Estado(self):
		print("Clase: Mago")
		super().Estado()

	def Atacar(self, objectivo):
		objectivo.vida -= self.inteligencia*0.6
		print(f"Vida actual del objetivo es: {objectivo.vida}")

class Guerrero(Personaje):

	def __init__(self, nombre):
		super().__init__(nombre)

		self.vida = 200
		self.Fuerza = 75
		self.inventario = ["Pocion de vida", "Escudo", "Espada"]

	def Estado(self):
		print("Clase: Guerrero")
		super().Estado()

	def Atacar(self, objectivo):
		objectivo.vida -= self.Fuerza*0.8
		print(f"El objetivo se ha quedado con {objectivo.vida} puntos de vida")

guerrero = Guerrero("Pedro")
mago = Mago("Yuto")

guerrero.Estado()
mago.Estado()

guerrero.Obtener_inventario()
mago.Obtener_inventario()

guerrero.Atacar(mago)
mago.Atacar(guerrero)