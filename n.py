class producto:
    counter = 0
    iva = 0.19
    def __init__(self, nombre, precio):
        self.nombre = nombre 
        self.precio = precio
        self.iva = self.precio * self.iva
        producto.counter+=1
    def getnombre(self):
        return self.nombre
    def getprecio(self):
        return self.precio
    def getiva(self):
        return self.iva
    def getall(self):
        return self.nombre, self.precio, self.iva + self.precio
    def setNombre(self, nombre):
        self.nombre = nombre 
    def setPrecio(self, precio):
        self.precio = precio
        
pro1 = producto('Televisor',10000000)
pro2 = producto('Celular',800000)
print(pro1.getall())
print(pro2.getall())
print("Contador",producto.counter)