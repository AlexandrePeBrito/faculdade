""" •	Para uma edição sabemos volume, número, mês, ano, tema
e artigos submetidos e selecionados. """

class Edicao():

    def __init__(self,volume,numero,mes,ano,tema):
        self.__volume=volume
        self.__numero=numero
        self.__mes=mes
        self.__ano=ano
        self.__tema=tema

    def getVolume(self):
        return self.__nome

    def setVolume(self,volume):
        self.__volume=volume

    def getNumero(self):
        return self.__numero

    def setNumero(self,numero):
        self.__numero=numero

    def getMes(self):
        return self.__mes

    def setMes(self,mes):
        self.__mes=mes

    def getAno(self):
        return self.__ano

    def setAno(self,ano):
        self.__ano=ano
    
    def getTema(self):
        return self.__tema

    def setTema(self,tema):
        self.__tema=tema