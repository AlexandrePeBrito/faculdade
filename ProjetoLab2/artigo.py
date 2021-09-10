""" •	Para o artigo sabemos os autores, o título e o arquivo contendo o artigo """

class Artigo:
    contador=0
    def __init__(self,autor,titulo,arquivo):
        self.__autor=autor
        self.__titulo=titulo
        self.__arquivo=arquivo
        self.__id=Artigo.contador+1

        Artigo.contador+=1

    def getAutor(self):
        return self.__autor

    def setAutor(self,autor):
        self.__autor=autor

    def getTitulo(self):
        return self.__titulo

    def setTitulo(self,titulo):
        self.__titulo=titulo

    def getArquivo(self):
        return self.__arquivo

    def setArquivo(self,arquivo):
        self.__arquivo=arquivo

    def getAutor(self):
        return self.__id