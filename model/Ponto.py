class Ponto(object):

    def __init__(self, x, y):
        self._x = x
        self._y = y

    #metodos get
    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    #metodos SET
    @y.setter
    def y(self,value):
        self._y = value

    @x.setter
    def x(self,value):
        self._x = value
