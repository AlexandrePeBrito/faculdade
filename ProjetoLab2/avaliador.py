""" •	De um avaliador deseja-se saber o nome, e-mail e 
temas para os quais está habilitado a avaliar artigos. """

class Avaliador():

    def __init__(self,nome,email,tema): #Construtor com as variaveis privates
        self.__nome=nome                
        self.__email=email
        self.__tema=tema
        