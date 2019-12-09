from pydoc import visiblename
import tkinter as tk
from tkinter import Event

from model.Poligono import Poligono
from model.Ponto import Ponto
from view.MainView import MainView
from ultils.ViewUtils import ViewUtils
from ultils.PoligonoUtils import PoligonoUtils
from controller.PoligonoController import PoligonoController


class TelaController(object):

    def __init__(self, view: object, canvas: object) -> object:
        self._view = view
        self._canvas = canvas
        self.setActionsInCanvas()
        self._polUtils = PoligonoUtils()
        self._viewUtils = ViewUtils()
        self._poligonoController = PoligonoController(canvas)
        self._poligonoSelecionado = None
        self._pontoAnterior = None
        self._index = 0

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

    def novoPoligono(self, event):
        p = Ponto(event.x, event.y)
        pol = self._polUtils.gerarPoligono(p, 50, 4)
        self._poligonoController.addPoligono(pol)
        self._viewUtils.drawPoligono(pol, canvas)
        return None

    def selecionaPoligono(self, event):
        click = Ponto(event.x, event.y)
        self._poligonoSelecionado = self._poligonoController.selectPoligono(click)
        self.drawPoligonoSelecionado(self._poligonoSelecionado)

    def drawPoligonoSelecionado(self, poligono: Poligono):
        canvas.delete('all')
        for pol in self._poligonoController.listPoligonos:
            if pol is poligono:
                self._viewUtils.drawSelectPoligono(pol, canvas)
            else:
                self._viewUtils.drawPoligono(pol, canvas)

    def clear(self, event):
        print(event.x, event.y)
        canvas.delete('all')

    def limparTela(self):
        canvas.delete('all')

    def drawTela(self, event):
        for pol in self._poligonos:
            self._viewUtils.drawPoligono(pol, canvas)

    def rotacioanrPoligono(self, event):
        if self._pontoAnterior == None:
            self.gravarPoligonoSelecionado()
            self._pontoAnterior = Ponto(event.x, event.y)
            self._index = self._poligonoController.listPoligonos.index(self._poligonoSelecionado)
        else:
            novo = Ponto(event.x, event.y)
            self._poligonoSelecionado = self._poligonoController.rotacionarPoligono(self._poligonoSelecionado,self._pontoAnterior, novo)
            self._pontoAnterior = novo
            self.limparTela()
            self.drawPoligonoSelecionado(self._poligonoSelecionado)

    def teste(self,e):
        print(e.x,e.y)
    def setActionsInCanvas(self):
        canvas.bind("<Control-Button-1>", lambda e: self.novoPoligono(e))
        canvas.bind('<Button-1>', lambda e: self.selecionaPoligono(e))
        canvas.bind("<Button-2>", lambda e: self.clear(e))
        canvas.bind("<Button-3>", lambda e: self.drawTela(e))
        canvas.bind('<Shift-B1-Motion>', lambda e: self.rotacioanrPoligono(e))

    def gravarPoligonoSelecionado(self):
        if (self._poligonoSelecionado != None):
            self._poligonoController.listPoligonos[self._index] = self._poligonoSelecionado
        self._pontoAnterior = None


tela = MainView()
canvas = tela.getCanvas()
telaC = TelaController(tela, canvas)
telaC.iniciarTela()
