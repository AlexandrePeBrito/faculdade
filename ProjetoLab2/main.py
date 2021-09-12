import edicao as ed
import artigo as ar
import autor  as au
import avaliador  as av
import revista  as re
import auxiliar as aux


artigos=[]
artigosAprovados=[]
artigosReprovados=[]
avaliadores=[]
autores=[]
edicao=[]
revista=[]

def inserirEdicao():
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
    revista=re.Revista(edicao)

    #Mostra para o usuario todas as edições
    print("Edições da Revista:\n")
    if len(revista.getColecao())==1:
        print(f"\t{revista.getColecao()[0].dadosEdicao()}")
    elif len(revista.getColecao())==0:
        print("Esta Revista não tem edições")      
    else:
        for i in range(0,len(revista.getColecao())):
            print(f"\t{revista.getColecao()[i].dadosEdicao()}")
    try:
        menuEdicao=int(input("\nDigite o numero referente a EDIÇÃO que deseja visualizar: "))
    
        #Mostrar os artigos submetidos
        print("\nO titulo do(s) Artigo(s) submetidos:\n")
        try:
            if len(revista.getColecao()[menuEdicao-1].getArtigosSubmetidos())==1:
                print(f"\t{revista.getColecao()[menuEdicao-1].getArtigosSubmetidos()[0].getTitulo()}")
            elif len(revista.getColecao()[menuEdicao-1].getArtigosSubmetidos())==0:
                print("\tNenhum artigo foi submetido")
            else:
                for c in range(0,len(revista.getColecao()[menuEdicao-1].getArtigosSubmetidos())):
                    print(f"\t{revista.getColecao()[menuEdicao-1].getArtigosSubmetidos()[c].getTitulo()}")
        except TypeError:
            print("\tNenhum artigo foi submetido")

        #Mostrar os artigos Aprovado
        print("\nO titulo do(s) Artigo(s) Aprovados:\n")
        try:
            if len(revista.getColecao()[menuEdicao-1].getArtigosAprovados())==1:
                print(f"\t{revista.getColecao()[menuEdicao-1].getArtigosAprovados()[0].getTitulo()}")
            elif len(revista.getColecao()[menuEdicao-1].getArtigosAprovados())==0:
                print("\tNenhum artigo submetido foi Aprovado")
            else:
                for c in range(0,len(revista.getColecao()[menuEdicao-1].getArtigosAprovados())):
                    print(f"\t{revista.getColecao()[menuEdicao-1].getArtigosAprovados()[c].getTitulo()}")
        except TypeError:
            print("\tNenhum artigo foi submetido")

        #Mostrar os artigos Reprovados
        print("\nO titulo do(s) Artigo(s) Reprovados:\n")
        
        try:
            artigosReprovados=list(set(revista.getColecao()[menuEdicao-1].getArtigosSubmetidos()) - set(revista.getColecao()[menuEdicao-1].getArtigosAprovados()))
        
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

def menu():
    c=0
    respMenu=1
    while respMenu!=0:
        if c==0:
            avaliadores, autores, artigos, revista = inserirEdicao()
        else:
            respMenu=input("\n\nMenu:\t1- Visualizar Avaliadores"+
            "\n\t\t2- Visualizar Autores"+
            "\n\t\t3- Visualizar Artigos"+
            "\n\t\t4- Visualizar Edições"+
            "\n\t\t5- sair")
            if respMenu==1:
                for c in range(0,len(avaliadores)):
                    print(avaliadores[c].dadosAvaliador())
            elif respMenu==2:
                for c in range(0,len(autores)):
                    print(autores[c].dadosAutor())
            elif respMenu==3:
                for c in range(0,len(artigos)):
                    print(artigos[c].dadosArtigo())
            elif respMenu==4:
                pass
            elif respMenu==5:
                print("\nObrigado por utilizar do nosso Sistema!!")
                exit(1)
