from copy import copy, deepcopy
from model.Ponto import Ponto
import math as m

class PontoUtils():

    def getClone(self, ponto):
        return deepcopy(ponto)

    def equals(self,pontoA,PontoB):
        return pontoA.x() == PontoB.x() and pontoA.y() == PontoB.y()

    def X2(self, ponto):
        return ponto.x ** 2

    def Y2(self, ponto):
        return ponto.y ** 2

    def multiMatriz(self, ponto, nlados):
        angulo = m.radians(360/nlados)
        x = (ponto.x * m.cos(angulo)) + (ponto.y * m.sin(angulo))
        y = (ponto.x * -m.sin(angulo)) + (ponto.y * m.cos(angulo))

        return Ponto(x,y);