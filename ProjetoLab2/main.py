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
    print("Edições da Revista:")
    if len(revista.getColecao())==0:
        print(f"\t{revista.getColecao()[0]}")
    else:
        for i in range(0,len(revista.getColecao())):
            print(f"\t{revista.getColecao()[i]}")
    menuEdicao=int(input("Digite o numero referente a EDIÇÃO que deseja visualizar: "))

    #Mostrar os artigos submetidos
    print("\nO titulo do(s) Artigo(s) submetidos:\n")
    if len(revista.getColecao()[menuEdicao].getArtigosSubmetidos())==0:
        print(f"\t{revista.getColecao()[menuEdicao].getArtigosSubmetidos()[0].getTitulo()}")
    else:
        for c in range(0,len(revista.getColecao()[menuEdicao].getArtigosSubmetidos())):
            print(f"\t{revista.getColecao()[menuEdicao].getArtigosSubmetidos()[c].getTitulo()}")

    #Mostrar os artigos Aprovado
    print("\nO titulo do(s) Artigo(s) Aprovados:\n")
    if len(revista.getColecao()[menuEdicao].getArtigosAprovados())==0:
        print(f"\t{revista.getColecao()[menuEdicao].getArtigosAprovados()[0].getTitulo()}")
    else:
        for c in range(0,len(revista.getColecao()[menuEdicao].getArtigosAprovados())):
            print(f"\t{revista.getColecao()[menuEdicao].getArtigosAprovados()[c].getTitulo()}")

    #Mostrar os artigos Reprovados
    artigosReprovados=list(set(revista.getColecao()[menuEdicao].getArtigosSubmetidos()) - set(revista.getColecao()[menuEdicao].getArtigosAprovados()))
    
    print("\nO titulo do(s) Artigo(s) Reprovados:\n")
    if len(artigosReprovados)==0:
        print(f"\t{artigosReprovados[0].getTitulo()}")
    else:
        for c in range(0,len(artigosReprovados)):
            print(f"\t{artigosReprovados[c].getTitulo()}")



