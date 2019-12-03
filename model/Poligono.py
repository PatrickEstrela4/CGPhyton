from model import Ponto

class Poligono(object):

    def __init__(self,centro,raio,nlados):
        self.centro = centro
        self.raio = raio
        self.vertices = None
        self.nlados = nlados

    @property
    def nlados(self):
        return nlados

    @property
    def vertices(self):
        return vertices

    @property
    def centro(self):
        return centro

    @property
    def raio(self):
       return raio

    @nlados.setter
    def nlados(self,nlados):
        self.nlados = nlados

    @vertices.setter
    def vertices(self,vertices):
        self.vertices = vertices

    @centro.setter
    def centro(self,centro):
        self.centro = centro

    @raio.setter
    def Raio(self,raio):
       self.raio = raio
    
    def addPonto(self, ponto):
        if isinstance(ponto,Ponto) :
            self.vertices.append(ponto)
        else:
            print('não é um ponto que foir adicionado')