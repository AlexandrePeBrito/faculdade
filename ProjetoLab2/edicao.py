""" •	Para uma edição sabemos volume, número, mês, ano, tema
e artigos submetidos e selecionados. """
from random import randint
import datetime

class Edicao():
    id=1

    def __init__(self,tema,artigosSubmetidos,artigosAprovados):
        date = datetime.date.today()
        self.__volume=Edicao.id
        self.__numero=randint(1,500)
        self.__mes=date.month
        self.__ano= date.year
        self.__tema=tema
        self.__artigosSubmetidos=artigosSubmetidos
        self.__artigosAprovados=artigosAprovados
        Edicao.id+=1

    def getVolume(self):
        return self.__nome

    def getNumero(self):
        return self.__numero

    def getMes(self):
        return self.__mes

    def getAno(self):
        return self.__ano
    
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

