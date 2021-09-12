""" •	De um avaliador deseja-se saber o nome, e-mail e 
temas para os quais está habilitado a avaliar artigos. """

class Avaliador():

    def __init__(self,nome,email,tema): #Construtor com as variaveis privates
        self.__nome=nome                
        self.__email=email
        self.__tema=tema

    def getNome(self):
        return self.__nome

    def setNome(self,nome):
        self.__nome=nome

    def getEmail(self):
        return self.__email

    def setEmail(self,email):
        self.__email=email

    def getTema(self):
        return self.__tema

    def setTema(self,tema):
        self.__tema=tema

    def dadosAvaliador(self):
        print(f"Avaliador:\n\tNome: {self.__nome}\n\tEmail: {self.__email}\n\tTema: {self.__tema}\n\n")

