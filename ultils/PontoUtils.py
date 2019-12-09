import math
from copy import copy, deepcopy
from model.Ponto import Ponto
import math as m


class PontoUtils():

    def getClone(self, ponto):
        return deepcopy(ponto)

    def equals(self, pontoA, PontoB):
        return pontoA.x() == PontoB.x() and pontoA.y() == PontoB.y()

    def multiMatriz(self, ponto: Ponto, nlados: object) -> object:
        angulo = m.radians(360 / nlados)
        x = (ponto.x * m.cos(angulo)) + (ponto.y * m.sin(angulo))
        y = (ponto.x * -m.sin(angulo)) + (ponto.y * m.cos(angulo))

        return Ponto(x, y);

    def multiMatriz2(self, ponto: Ponto, angulo: object) -> object:
        angulo = m.radians(angulo)
        x = (ponto.x * m.cos(angulo)) + (ponto.y * m.sin(angulo))
        y = (ponto.x * -m.sin(angulo)) + (ponto.y * m.cos(angulo))

        return Ponto(x, y);

    def distanciaPolPonto(self, pontoA: Ponto, pontoB: Ponto, pontoC: Ponto):
        r = (pontoB.y - pontoA.y)
        s = -(pontoB.x - pontoA.x)
        t = (pontoB.x * pontoA.y) - (pontoB.y * pontoA.x)

        m = -r / s
        b = -t / s

        m2 = s / r
        b2 = (pontoC.y - ((s / r) * pontoC.x))

        x = (b2 - b) / (m - m2)
        y = ((b2 * m) - (b * m2)) / (m - m2)

        p = Ponto(x, y)

        if round(s, 0) == 0:
            p = Ponto(pontoB.x, pontoC.y)

        if round(r, 0) == 0:
            p = Ponto(pontoC.x, pontoB.y)

        if self.equacaoPonto(pontoA, pontoB, p):
            return self.distanciaPontoReta(p, pontoC)

        return 100

    def equacaoPonto(self, pontoA: Ponto, pontoB: Ponto, pontoC: Ponto):
        if (pontoB.y == pontoA.y) and (pontoC.y == pontoA.y):
            if (max(pontoB.x, pontoA.x) > pontoC.x) and (min(pontoB.x, pontoA.x) < pontoC.x):
                return True

        if (pontoB.x == pontoA.x) and (pontoC.x == pontoA.x):
            if (max(pontoB.y, pontoA.y) > pontoC.y) and (min(pontoB.y, pontoA.y) < pontoC.y):
                return True

        t = (pontoC.x - pontoA.x) / (pontoB.x - pontoA.x)
        t2 = (pontoC.y - pontoA.y) / (pontoB.y - pontoA.y)

        return (0 <= t <= 1) and (0 <= t2 <= 1)

    def distanciaPontoReta(self, pontoA: Ponto, pontoB: Ponto):
        return math.sqrt(((pontoA.x - pontoB.x) * (pontoA.x - pontoB.x) + (pontoA.y - pontoB.y) * (pontoA.y - pontoB.y)))

    def printPonto(self, p: Ponto):
        print(p.x, " ", p.y)

    def anguloVetores(self, pontoA: Ponto, pontoB: Ponto, pontoC: Ponto):
        vetorA = Ponto((pontoB.x - pontoA.x), (pontoB.y - pontoA.y))
        vetorB = Ponto((pontoC.x - pontoA.x), (pontoC.y - pontoA.y))

        ret = ((vetorA.x * vetorB.x) + (vetorB.y * vetorA.y)) / \
              (math.sqrt(vetorA.x * vetorA.x + vetorA.y * vetorA.y) * math.sqrt(
                  vetorB.x * vetorB.x + vetorB.y * vetorB.y))

        if self.calculaDirecao(vetorA, vetorB):
            return math.degrees(math.acos(ret))
        else:
            return -math.degrees(math.acos(ret))

    def calculaDirecao(self, vetorA: Ponto, vetorB: Ponto):
        x = (vetorB.y * vetorA.x) - (vetorB.x * vetorA.y)
        if x < 0:
            return True
        else:
            return False


