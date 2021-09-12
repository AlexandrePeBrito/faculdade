import edicao as ed
import artigo as ar
import autor  as au
import avaliador  as av
import revista  as re
import auxiliar as aux


artigosAprovados=[]
artigosReprovados=[]

def inserirEdicao(revista):
    #Inserindo os dados
    avaliadores=aux.inserirAvaliadores()                                   
    autores=aux.inserirAutores()                                        
    artigos=aux.inserirArtigos(autores)                                       
    edicao=aux.inserirEdicao(artigos)

    #Dando as notas para os artigos  
    try:                                  
        for c in range(0,len(artigos)):
            re.AvaliarArtigo(artigos[c],avaliadores,edicao) 
            if(artigos[c].getNota()>=7): artigosAprovados.append(artigos[c])
        
        #Setando os artigos aprovados 
        edicao.setArtigosAprovados(artigosAprovados)
    except TypeError:
        print("Nenhum artigo foi Submetido nesta edição")
    #publicando a edição na revista
    if(revista==None):
        revista=re.Revista(edicao)
    else:
        revista.setColecao(edicao)

    #Mostra para o usuario todas as edições
    print("Edição da Revista:\n")
    if len(revista.getColecao())==1:
        print(f"\t{revista.getColecao()[0].dadosEdicao()}")
    elif len(revista.getColecao())==0:
        print("Esta Revista não tem edições")      
    else:
        print(f"\t{revista.getColecao()[len(revista.getColecao())-1].dadosEdicao()}")
    try:    
        #Mostrar os artigos submetidos
        print("\nO titulo do(s) Artigo(s) submetidos:\n")
        try:
            if len(revista.getColecao()[len(revista.getColecao())-1].getArtigosSubmetidos())==1:
                print(f"\t{revista.getColecao()[len(revista.getColecao())-1].getArtigosSubmetidos()[0].getTitulo()}")
            elif len(revista.getColecao()[len(revista.getColecao())-1].getArtigosSubmetidos())==0:
                print("\tNenhum artigo foi submetido")
            else:
                for c in range(0,len(revista.getColecao()[len(revista.getColecao())-1].getArtigosSubmetidos())):
                    print(f"\t{revista.getColecao()[len(revista.getColecao())-1].getArtigosSubmetidos()[c].getTitulo()}")
        except TypeError:
            print("\tNenhum artigo foi submetido")

        #Mostrar os artigos Aprovado
        print("\nO titulo do(s) Artigo(s) Aprovados:\n")
        try:
            if len(revista.getColecao()[len(revista.getColecao())-1].getArtigosAprovados())==1:
                print(f"\t{revista.getColecao()[len(revista.getColecao())-1].getArtigosAprovados()[0].getTitulo()}")
            elif len(revista.getColecao()[len(revista.getColecao())-1].getArtigosAprovados())==0:
                print("\tNenhum artigo submetido foi Aprovado")
            else:
                for c in range(0,len(revista.getColecao()[len(revista.getColecao())-1].getArtigosAprovados())):
                    print(f"\t{revista.getColecao()[len(revista.getColecao())-1].getArtigosAprovados()[c].getTitulo()}")
        except TypeError:
            print("\tNenhum artigo foi submetido")

        #Mostrar os artigos Reprovados
        print("\nO titulo do(s) Artigo(s) Reprovados:\n")
        
        try:
            artigosReprovados=list(set(revista.getColecao()[len(revista.getColecao())-1].getArtigosSubmetidos()) - set(revista.getColecao()[len(revista.getColecao())-1].getArtigosAprovados()))
        
            if len(artigosReprovados)==1:
                print(f"\t{artigosReprovados[0].getTitulo()}")
            elif len(artigosReprovados)==0:
                print("\t Todos os artigos Submetidos foram Aprovados Ou não submeteram nenhum artigo")
            else:
                for c in range(0,len(artigosReprovados)):
                    print(f"\t{artigosReprovados[c].getTitulo()}")
        except TypeError:
            print("\tNenhum artigo foi submetido")
    except ValueError:
        print("Você inseriu um valor invalido!")
    return avaliadores, autores, artigos, revista



def acessarEdicao(revista,edicao):
    respMenu=1
    while respMenu!=0:
        respMenu=int(input("\n\nMenu:\t\t1- Visualizar Artigos"+
            "\n\t\t0- sair"))
        if respMenu==1:
            try:
                for c in range(0,len(revista.getColecao()[edicao-1].getArtigosSubmetidos())):
                    print(revista.getColecao()[edicao-1].getArtigosSubmetidos()[c].dadosArtigo())
                    c+=1
            except TypeError:
                print("Nenhum Artigo foi submetido")   
        elif respMenu==0:
            print("\nObrigado por utilizar do nosso Sistema!!")   


def menu():
    c=0
    respMenu=1
    while respMenu!=0:
        if c==0:
            avaliadores, autores, artigos, revista = inserirEdicao(None)
            c+=1
        else:
           
            respMenu=int(input("\n\nMenu:\t\t1- Visualizar Avaliadores desta Edição"+
            "\n\t\t2- Visualizar Autores desta Edição"+
            "\n\t\t3- Visualizar Artigos desta Edição"+
            "\n\t\t4- Visualizar todas as Edições"+
            "\n\t\t5- Acessar outra Edição"
            "\n\t\t6 Criar mais uma Edição"+
            "\n\t\t0- sair"))
            if respMenu==1:
                for c in range(0,len(avaliadores)):
                    print(avaliadores[c].dadosAvaliador())
                    c+=1
            elif respMenu==2:
                for c in range(0,len(autores)):
                    print(autores[c].dadosAutor())
                    c+=1
            elif respMenu==3:
                try:
                    for c in range(0,len(artigos)):
                        print(artigos[c].dadosArtigo())
                        c+=1
                except TypeError:
                    print("Nenhum Artigo foi submetido")
                    c+=1
            elif respMenu==4:
                for c in range(0,len(revista.getColecao())):
                    print(revista.getColecao()[c].dadosEdicao())
                    c+=1
            elif respMenu==5:
                volEdicao=int(input("Informe o volume da Edição que deseja acessar: "))
                acessarEdicao(revista,volEdicao)
            elif respMenu==6:
                avaliadores, autores, artigos, revista = inserirEdicao(revista)
                c+=1
            elif respMenu==0:
                print("\nObrigado por utilizar do nosso Sistema!!")
                exit(1)

menu()