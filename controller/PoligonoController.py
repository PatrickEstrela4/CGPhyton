from model.Poligono import Poligono
from model.Ponto import Ponto
from ultils.PontoUtils import PontoUtils


class PoligonoController():

    def __init__(self, canvas):
        self._listPoligonos = []
        self._canvas = canvas
        self._poligono = None
        self._pontoUtils = PontoUtils()

    @property
    def listPoligonos(self):
        return self._listPoligonos

    @property
    def canvas(self):
        return self._canvas

    @property
    def poligono(self):
        return self._poligono

    @listPoligonos.setter
    def listPoligonos(self, listPoligonos):
        self._listPoligonos = listPoligonos

    @canvas.setter
    def canvas(self, canvas):
        self._canvas = canvas

    @poligono.setter
    def poligono(self, poligono):
        self._poligono = poligono

    def addPoligono(self, poligono: Poligono):
        self._listPoligonos.append(poligono)

    def selectPoligono(self, p: Ponto):

        menor = 1000000000000
        distancia1 = 0

        for pol in self._listPoligonos:
            nlados = pol.nlados

            for i in range(1, nlados):
                distancia1 = self._pontoUtils.distanciaPolPonto(pol.vertices[i], pol.vertices[i - 1], p)
                if distancia1 < menor:
                    if distancia1 < 10:
                        retorno = pol
                        menor = distancia1

            distancia1 = self._pontoUtils.distanciaPolPonto(pol.vertices[0], pol.vertices[nlados - 1], p)
            if distancia1 < menor:
                if distancia1 < 10:
                    retorno = pol
                    menor = distancia1

        try:
            retorno
        except NameError:
            retorno = None
        return retorno

    def rotacionarPoligono(self, selecionado: Poligono, anterior: Ponto, novo: Ponto):
        xc = selecionado.centro.x
        yc = selecionado.centro.y

        angulo = self._pontoUtils.anguloVetores(selecionado.centro, anterior, novo)

        for ponto in selecionado.vertices:
            ponto.x = ponto.x - xc
            ponto.y = ponto.y - yc

        for ponto in selecionado.vertices:
            ponto2 = self._pontoUtils.multiMatriz2(ponto, angulo)
            ponto.x = ponto2.x
            ponto.y = ponto2.y
            print(ponto)

        for ponto in selecionado.vertices:
            ponto.x = ponto.x + xc
            ponto.y = ponto.y + yc

        return selecionado

    def transladarPoligono(self, selecionado: Poligono, anterior: Ponto, novo: Ponto):
        y = novo.y - anterior.y
        x = novo.x - anterior.x

        print(x, " ", y)
        for pol in selecionado.vertices:
            pol.x = pol.x + x
            pol.y = pol.y + y

        selecionado.centro.setXY((selecionado.centro.x + x), (selecionado.centro.y + y))

        return selecionado

    def escalaPoligono(self, original: Poligono, selecionado: Poligono, inicio: Ponto, fim: Ponto):

        prop = self._pontoUtils.distanciaPontoReta(selecionado.centro, fim) / \
               self._pontoUtils.distanciaPontoReta(selecionado.centro, inicio)

        xc = selecionado.centro.x
        yc = selecionado.centro.y

        for ponto in selecionado.vertices:
            ponto.x = ponto.x - xc
            ponto.y = ponto.y - yc

        for ponto in original.vertices:
            ponto.x = ponto.x - xc
            ponto.y = ponto.y - yc

        i = 0

        for ponto in selecionado.vertices:
            ponto.setXY(original.vertices[i].x * prop, original.vertices[i].y * prop)
            i += 1

        for ponto in selecionado.vertices:
            ponto.x = ponto.x + xc
            ponto.y = ponto.y + yc

        for ponto in original.vertices:
            ponto.x = ponto.x + xc
            ponto.y = ponto.y + yc

        return selecionado
