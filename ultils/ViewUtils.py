import tkinter as tk
from model.Ponto import Ponto
from model.Poligono import Poligono


class ViewUtils():

    def key(event):
        print("pressed", repr(event.char))

    def getClick(event):
        return Ponto(event.x, event.y)

    def drawline(self, pontoA: Ponto, pontoB: Ponto, canvas):
        canvas.create_line(pontoA.x, pontoA.y, pontoB.x, pontoB.y)
        canvas.pack()

    def drawPoligono(self, poligono: Poligono, canvas):
        pontoA = None
        for pontoB in poligono.vertices:
            if (pontoA == None):
                pontoA = pontoB
                continue
            self.drawline(pontoA, pontoB, canvas)
            pontoA = pontoB
        self.drawline(pontoA, poligono.vertices[0], canvas)
