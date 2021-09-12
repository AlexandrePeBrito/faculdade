""" •	Os autores devem informar, além de seus nomes, e-mails 
e as instituições a que pertencem com endereço """

class Autor():
    def __init__(self,nome,email,instituicao,endereco):
        self.__nome=nome
        self.__email=email
        self.__instituicao=instituicao
        self.__endereco=endereco

    def getNome(self):
        return self.__nome

    def setNome(self,nome):
        self.__nome=nome

    def getEmail(self):
        return self.__email

    def setEmail(self,email):
        self.__email=email

    def getInstituicao(self):
        return self.__instituicao

    def setInstituicao(self,instituicao):
        self.__instituicao=instituicao

    def getEndereco(self):
        return self.__endereco

    def setEndereco(self,endereco):
        self.__endereco=endereco

    def dadosAutor(self):
        print(f"Autor:\n\tNome: {self.__nome}\n\tEmail: {self.__email}\n\tInstituição: {self.__instituicao}\n\tEndereço: {self.__endereco}\n\n")