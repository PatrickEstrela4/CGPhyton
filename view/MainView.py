import tkinter as tk

class MainView(object):

    def __init__(self) -> object:
        self.janela = tk.Tk()
        self.janela.title("CG em python")
        self.janela["bg"] = "white"
        self.tamanhoTela = "" + str(self.janela.winfo_screenwidth()) + "x" + str(
            self.janela.winfo_screenheight()) + "+0+0"
        self.janela.geometry("600x800+300+300")
        self.canvas = tk.Canvas(self.janela, width=self.janela.winfo_screenwidth(),
                                height=self.janela.winfo_screenheight())
        self.canvas.pack()

    def iniciar(self):
        self.janela.mainloop()

    def getCanvas(self):
        return self.canvas

    def getJanela(self):
        return self.janela
