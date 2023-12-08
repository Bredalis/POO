
class Camiseta:

	def __init__(self, talla, color, precio, marca):

		# Propiedades de las camisetas

		self.talla = talla
		self.color = color
		self.precio = precio
		self.marca = marca
		self.rebajada = False

	def Descuento(self, porcentaje): 
		self.precio = self.precio - self.precio*porcentaje/100

		# Mostrar precio rebajado (descuento)

		if porcentaje < 100:
			self.rebajada = True

	def Informacion(self):

		"""
		Mostrar info sobre 
		las camisetas y 
		si tiene rebaja o no
		"""

		info = f"\nDescripcion de la camiseta: \nMarca: {self.marca} \
		\nPrecio: {self.precio:.2f} \nColor: {self.color} \nTalla: {self.talla} \n"

		if self.rebajada:
			info += "\nEste producto esta rebajado"

		else:
			info += "\nEste producto no esta rebajado"

		return info

camiseta_gucci = Camiseta("M", "Negro", 100, "Gucci")
camiseta_adidas = Camiseta("M", "Rojo", 30, "Adidas")

camiseta_gucci.Descuento(20)
camiseta_adidas.Descuento(50)

print(camiseta_gucci.Informacion())
print(camiseta_adidas.Informacion())