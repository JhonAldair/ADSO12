class madre:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    def presentarse(self):
        print('yo soy',self.nombre,'y tengo',self.edad,'años de edad')
mimadre=madre('bulma',35)
mimadre.presentarse()
class padre(madre):
        def __init__(self,nombre,edad):
            self.nombre=nombre
            self.edad=edad
mipadre=padre('vegeta',33)
mipadre.presentarse()