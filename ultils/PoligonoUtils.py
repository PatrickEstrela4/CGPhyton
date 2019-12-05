from copy import deepcopy
from model.Ponto import Ponto
from model.Poligono import Poligono
from ultils.PontoUtils import PontoUtils


class PoligonoUtils():

    def getClone(self, poligono):
        return deepcopy(poligono)

    def calcCentro(self, poligonos):

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

        return Ponto(x, y)

    def gerarPoligono(self, centro, raio, nlados):
        ponto = Ponto(0, -raio)
        poligono = Poligono(centro, raio, nlados)

        poligono.addPonto(ponto)

        pontoUtils = PontoUtils

        for i in range(-nlados, -1):
            ponto = pontoUtils.multiMatriz(self, poligono.vertices[-1], nlados)

            poligono.addPonto(ponto)

        for vertice in poligono.vertices:
            vertice.x = (centro.x + vertice.x)
            vertice.y = (centro.y + vertice.y)

        return poligono
