from copy import deepcopy
from model.Ponto import Ponto
from model.Poligono import Poligono
from ultils.PontoUtils import PontoUtils

class PoligonoUtils():
    
    def getClone(self, poligono):
        return deepcopy(poligono)

    def calcCentro(self,poligonos):
        maxX = 0
        maxY = 0
        minX = 0
        minY = 0

        maxX = poligonos[0].x()
        maxY = poligonos[0].y()
        minX = poligonos[0].x()
        minY = poligonos[0].y()

        for poligono in poligonos:
            if maxX < poligonos[0].x():
                maxX = poligonos[0].x()
            
            if maxY < poligonos[0].y():
                maxY = poligonos[0].y()

            if minX > poligonos[0].x():
                minX = poligonos[0].x()

            if maxX > poligonos[0].x():
                maxX = poligonos[0].x()
        
        x = (maxX + minX) / 2
        y = (maxY + minY) / 2

        return Ponto(x,y)

    def gerarPolitico(self, centro, raio,nlados):
        ponto = Ponto(0,-raio)
        poligono = Poligono(centro,raio,nlados)

        for i in nlados:
            p = PontoUtils.multiMatriz(poligono.vertices[-1])

            poligono.addPonto(p)

        for vertice in poligono.vertices:
            vertice.x = (centro.x + vertice.x)
            vertice.y = (centro.y + vertice.y)

        return poligono