import artigo as ar
import autor  as au
import avaliador  as av




def inserirAutores():
    autores=[]
    respAU=1
    c=0
    while respAU!=0:
        print("\n")
        nome=input("Informe o nome do Autor: ")
        email=input("Informe o Email do Autor: ")
        instituicao=input("Informe a instituição do Autor: ")
        endereco=input("Informe o endereço do Autor: ")
        autores.append(au.Autor(nome,email,instituicao,endereco))
        respAU=int(input("Para Parar de inserir Avaliador Aperte 0."))
    return autores

def inserirArtigos(autores):
    artigos=[]
    respAR=1
    while respAR!=0:
        for c in range(0,len(autores)):print(f'{c+1}- {autores[c].getNome()}')
        autor=int(input("Informe o numero correspondente ao Autor: "))
        titulo=input("Informe o Titulo do Artigo: ")
        arquivo=None
        artigos.append(ar.Artigo(autores[autor-1],titulo,arquivo))
        respAR=int(input("Para Parar de inserir Avaliador Aperte 0."))
    return artigos
def inserirEdicao():
    pass

def inserirAvaliadores():
    Avaliadores=[]
    respAV=1
    c=0
    while respAV!=0:
        print("\n")
        nome=input("Informe o nome do Avaliador: ")
        email=input("Informe o Email do Avaliador: ")
        tema=input("Informe o Tema que o Avaliador ira avaliar: ")
        tema.lower()
        Avaliadores.append(av.Avaliador(nome,email,tema))
        c+=1
        if(c<3):
            respAV=1
        else:
            respAV=int(input("Para Parar de inserir Avaliador Aperte 0."))
    return Avaliadores










