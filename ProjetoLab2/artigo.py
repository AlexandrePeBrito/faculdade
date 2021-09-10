""" •	Para o artigo sabemos os autores, o título e o arquivo contendo o artigo """

class Artigo:
    contador=0
    def __init__(self,autor,titulo,arquivo):
        self.__autor=autor
        self.__titulo=titulo
        self.__arquivo=arquivo
        self.__id=Artigo.contador+1
        self.__nota=None
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

    def setNota(self,nota):
        self.__nota=nota

    def getNota(self):
        return self.__nota

    def getID(self):
        return self.__id

    def dadosArtigo(self):
        print(f'Artigo:\nID: {self.__id}\nAutor: {self.__autor.getNome()}\nTitulo: {self.__titulo}\nNota: {self.__nota}')
