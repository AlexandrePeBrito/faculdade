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
verif=1
menu=0

while verif!=0:
    #Inserindo os dados
    avaliadores=aux.inserirAvaliadores()                                   
    autores=aux.inserirAutores()                                        
    artigos=aux.inserirArtigos(autores)                                       
    edicao=aux.inserirEdicao(artigos)

    #Dando as notas para os artigos                                    
    for c in range(0,len(artigos)):
        re.AvaliarArtigo(artigos[c],avaliadores,edicao) 
        if(artigos[c].getNota()>=7): artigosAprovados.append(artigos[c])
    
    #Setando os artigos aprovados 
    edicao.setArtigosAprovados(artigosAprovados)

    #publicando a edição na revista
    revista=re.Revista(edicao)

    #Mostra para o usuario todas as edições
    print("Edições da Revista:\n\n")
    if len(revista.getColecao())==1:
        print(f"\t{revista.getColecao()[0].dadosEdicao()}")
    elif len(revista.getColecao())==1:
        print("Esta Revista não tem edições")
    else:
        for i in range(0,len(revista.getColecao())):
            print(f"\t{revista.getColecao()[i].dadosEdicao()}")
    menuEdicao=int(input("\nDigite o numero referente a EDIÇÃO que deseja visualizar: "))

    #Mostrar os artigos submetidos
    print("\nO titulo do(s) Artigo(s) submetidos:\n")
    if len(revista.getColecao()[menuEdicao-1].getArtigosSubmetidos())==1:
        print(f"\t{revista.getColecao()[menuEdicao-1].getArtigosSubmetidos()[0].getTitulo()}")
    else:
        for c in range(0,len(revista.getColecao()[menuEdicao-1].getArtigosSubmetidos())):
            print(f"\t{revista.getColecao()[menuEdicao-1].getArtigosSubmetidos()[c].getTitulo()}")

    #Mostrar os artigos Aprovado
    print("\nO titulo do(s) Artigo(s) Aprovados:\n")
    if len(revista.getColecao()[menuEdicao-1].getArtigosAprovados())==1:
        print(f"\t{revista.getColecao()[menuEdicao-1].getArtigosAprovados()[0].getTitulo()}")
    elif len(revista.getColecao()[menuEdicao-1].getArtigosAprovados())==0:
        print("\tNenhum artigo submetido foi Aprovado")
    else:
        for c in range(0,len(revista.getColecao()[menuEdicao-1].getArtigosAprovados())):
            print(f"\t{revista.getColecao()[menuEdicao-1].getArtigosAprovados()[c].getTitulo()}")

    #Mostrar os artigos Reprovados
    artigosReprovados=list(set(revista.getColecao()[menuEdicao-1].getArtigosSubmetidos()) - set(revista.getColecao()[menuEdicao-1].getArtigosAprovados()))
    
    print("\nO titulo do(s) Artigo(s) Reprovados:\n")
    if len(artigosReprovados)==1:
        print(f"\t{artigosReprovados[0].getTitulo()}")
    elif len(artigosReprovados)==0:
        print("\t Todos os artigos Submetidos foram Aprovados")
    else:
        for c in range(0,len(artigosReprovados)):
            print(f"\t{artigosReprovados[c].getTitulo()}")



