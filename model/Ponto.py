class Ponto(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    #metodos get
    @property
    def x(self):
        return x

    @property
    def y(self):
        return y

    #metodos SET
    @y.setter
    def y(self,value):
        self.y = value

    @x.setter
    def x(self,value):
        self.x = value
