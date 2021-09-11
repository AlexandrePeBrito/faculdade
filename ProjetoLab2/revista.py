#originalidade, conteúdo e apresentação

from random import randint


avaliador=[]

def AvaliarArtigo(artigo,avaliadores,edicao):
    i=0
    for c in range(0,len(avaliadores)):
        if(avaliadores[c].getTema()==edicao.getTema()):
            avaliador.append(avaliadores[c])
            i+=1
    if(i<2):
        print("Esta edição não ocorrerá por falta de Avaliadores do tema")
        exit(1)
    else:    
        avaliador1=avaliador[0]
        avaliador2=avaliador[1]
        avaliador3=avaliador[2]

        print(f"Os avaliadores do Artigo '{artigo.getTitulo()}' sao: ")
        print(f"\nAvaliador1: {avaliador1.getNome()}")
        print(f"Avaliador2: {avaliador2.getNome()}")
        print(f"Avaliador3: {avaliador3.getNome()}")
        for c in range(0,3):
            notaAvaliador1=randint(0,10)
            notaAvaliador2=randint(0,10)
            notaAvaliador3=randint(0,10)
            if c==0: 
                print(f'\nEm originalidade os avaliadores deram a seguintes notas:\n'+
                f'Avaliador1 {avaliador1.getNome()} : {notaAvaliador1}\n'+
                f'Avaliador2 {avaliador2.getNome()} : {notaAvaliador2}\n'+
                f'Avaliador3 {avaliador3.getNome()} : {notaAvaliador3}\n')
                originalidade= (notaAvaliador1+notaAvaliador2+notaAvaliador3)/3
                print(f'Media final em Originalidade: {originalidade}')

            elif c==1: 
                print(f'\nEm conteudo os avaliadores deram a seguintes notas:\n'+
                f'Avaliador1 {avaliador1.getNome()} : {notaAvaliador1}\n'+
                f'Avaliador2 {avaliador2.getNome()} : {notaAvaliador2}\n'+
                f'Avaliador3 {avaliador3.getNome()} : {notaAvaliador3}\n')
                conteudo=(notaAvaliador1+notaAvaliador2+notaAvaliador3)/3
                print(f'Media final em Conteudo: {conteudo}')

            elif c==2: 
                print(f'\nEm apresentação os avaliadores deram a seguintes notas:\n'+
                f'Avaliador1 {avaliador1.getNome()} : {notaAvaliador1}\n'+
                f'Avaliador2 {avaliador2.getNome()} : {notaAvaliador2}\n'+
                f'Avaliador3 {avaliador3.getNome()} : {notaAvaliador3}\n')
                apresentação=(notaAvaliador1+notaAvaliador2+notaAvaliador3)/3
                print(f'Media final em Apresentação: {apresentação}')
        nota=(originalidade+conteudo+apresentação)/3
        print(f'\n\nNota final do Artigo: {nota}')
        artigo.setNota(nota)

class Revista():
    __colecao=[]
    def __init__(self,edicao):
        self.__colecao.append(edicao)

    def getColecao(self,):
        return self.__colecao

