""" •	Para o artigo sabemos os autores, o título e o arquivo contendo o artigo """

class Artigo:
    contador=0
    def __init__(self,autor,titulo,arquivo):
        self.__autor=autor
        self.__titulo=titulo
        self.__arquivo=arquivo
        self.__id=Artigo.contador+1
        Artigo.contador+=1
