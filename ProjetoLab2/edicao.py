""" •	Para uma edição sabemos volume, número, mês, ano, tema
e artigos submetidos e selecionados. """

class Edicao():

    def __init__(self,volume,numero,mes,ano,tema):
        self.__volume=volume
        self.__numero=numero
        self.__mes=mes
        self.__ano=ano
        self.__tema=tema
