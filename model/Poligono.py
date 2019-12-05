from model import Ponto

class Poligono(object):

    def __init__(self,centro,raio,nlados):
        self._centro = centro
        self._raio = raio
        self._vertices = None
        self._nlados = nlados

    @property
    def nlados(self):
        return self._nlados

    @property
    def vertices(self):
        return self._vertices

    @property
    def centro(self):
        return self._centro

    @property
    def raio(self):
       return self._raio

    @nlados.setter
    def nlados(self,nlados):
        self._nlados = nlados

    @vertices.setter
    def vertices(self,vertices):
        self._vertices = vertices

    @centro.setter
    def centro(self,centro):
        self._centro = centro

    @raio.setter
    def Raio(self,raio):
       self._raio = raio
    
    def addPonto(self, ponto):
        if self._vertices is None:
                self._vertices = []
        #if isinstance(ponto, Ponto):
        self._vertices.append(ponto)
        #else:
        #    print('não é um ponto que foir adicionado')