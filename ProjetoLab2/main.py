import edicao as ed
import artigo as ar
import autor  as au
import avaliador  as av
import revista  as re
import auxiliar as aux



artigos=[]
artigosAprovados=[]
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
    print("Edições da Revista:")
    
    #Mostrar os artigos de edição escolhida
    print("\nO titulo do(s) Artigo(s) submetidos:\n")
    if len(revista.getColecao()[0].getArtigosSubmetidos())==0:
        print(f"\t{revista.getColecao()[0].getArtigosSubmetidos()[0].getTitulo()}")
    else:
        for c in range(0,len(revista.getColecao()[0].getArtigosSubmetidos())):
            print(f"\t{revista.getColecao()[0].getArtigosSubmetidos()[c].getTitulo()}")




