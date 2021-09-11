""" •	Para uma edição sabemos volume, número, mês, ano, tema
e artigos submetidos e selecionados. """
from random import randint
import datetime

class Edicao():
    id=1

    def __init__(self,tema,artigosSubmetidos):
        date = datetime.date.today()
        self.__volume=Edicao.id
        self.__numero=randint(1,500)
        self.__mes=date.month
        self.__ano= date.year
        self.__tema=tema
        self.__artigosSubmetidos=artigosSubmetidos
        self.__artigosAprovados=[]
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
    
    def getArtigosSubmetidos(self):
        return self.__artigosSubmetidos

    def setArtigosSubmetidos(self,artigosSubmetidos):
        self.__artigosSubmetidos=artigosSubmetidos
    
    def getArtigosAprovados(self):
        return self.__artigosAprovados

    def setArtigosAprovados(self,artigosAprovados):
       self.__artigosAprovados=artigosAprovados

    def dadosEdicao(self):
        print(f"\tVolume: {self.__volume}"
        +f"\n\tNumero: {self.__numero}"
        +f"\n\tMes: {self.__mes}"
        +f"\n\tAno: {self.__ano}"
        +f"\n\tTema: {self.__tema}")

