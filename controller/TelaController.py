from pydoc import visiblename
import tkinter as tk
from model.Poligono import Poligono
from model.Ponto import Ponto
from view.MainView import MainView
from ultils.ViewUtils import ViewUtils
from ultils.PoligonoUtils import PoligonoUtils


class TelaController(object):

    def __init__(self, view: object, canvas: object) -> object:
        self._view = view
        self._canvas = canvas
        self.setActionsInCanvas()

    def iniciarTela(self):
        self._view.iniciar()

    @property
    def canvas(self):
        return self._canvas

    @property
    def view(self):
        return self._view

    @view.setter
    def view(self, view2):
        self._view = view2

    @canvas.setter
    def canvas(self, canvas2):
        self._canvas = canvas2

    def getClick(self,event):
        p = Ponto(event.x, event.y)
        ultil = PoligonoUtils()
        ultilv = ViewUtils()
        pol = ultil.gerarPoligono(p, 50, 4)
        ultilv.drawPoligono(pol, canvas)
        return None

    def setActionsInCanvas(self):
        canvas.bind("<Button-1>", lambda e: self.getClick(e))



tela = MainView()
canvas = tela.getCanvas()
telaC = TelaController(tela, canvas)
telaC.iniciarTela()





