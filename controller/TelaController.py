from pydoc import visiblename
import tkinter as tk
from model.Poligono import Poligono
from view.MainView import MainView
from ultils import ViewUtils


class TelaController(object):

    def __init__(self, view: object, canvas: object) -> object:
        self._view = view
        self._canvas = canvas

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


tela = MainView()
canvas = tela.getCanvas()
telaC = TelaController(tela, canvas)
# telaC.iniciarTela()
# p = telaC.canvas.bind("<Button 1>", ViewUtils.getClick())
# print(p.x, p.y)
