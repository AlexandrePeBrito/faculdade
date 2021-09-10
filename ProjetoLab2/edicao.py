""" •	Para uma edição sabemos volume, número, mês, ano, tema
e artigos submetidos e selecionados. """

class Edicao():

    def __init__(self,volume,numero,mes,ano,tema,artigosSubmetidos,artigosAprovados):
        self.__volume=volume
        self.__numero=numero
        self.__mes=mes
        self.__ano=ano
        self.__tema=tema
        self.__artigosSubmetidos=artigosSubmetidos
        self.__artigosAprovados=artigosAprovados

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
    
    def getTema(self):
        return self.__artigosSubmetidos

    def setTema(self,artigosSubmetidos):
        self.__artigosSubmetidos=artigosSubmetidos
    
    def getTema(self):
        return self.__artigosAprovados

    def setTema(self,artigosAprovados):
        self.__artigosAprovados=artigosAprovados

    def dadosEdicao(self):
        print(f"Edição:\nVolume: {self.__volume}\nNumero: {self.__numero}\nMes: {self.__mes}\n"+
        f"Ano: {self.__ano}\nTema: {self.__tema}\nArtigos Submetidos: ")
        for c in range(0,len(self.__artigosSubmetidos)): print(self.__artigosSubmetidos[c].getTitulo())
        #print(f"Artigos Aprovados: ")
        #for c in self.__artigosSubmetidos: print(self.__artigosSubmetidos)
