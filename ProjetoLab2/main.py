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
    avaliadores=aux.inserirAvaliadores()                                   
    autores=aux.inserirAutores()                                        
    artigos=aux.inserirArtigos(autores)                                       
    edicao=aux.inserirEdicao(artigos)
                                        
    for c in range(0,len(artigos)):
        re.AvaliarArtigo(artigos[c],avaliadores,edicao) 
        if(artigos[c].getNota()>=7): artigosAprovados.append(artigos[c]) 
    edicao.setArtigosAprovados(artigosAprovados)

    revista=re.Revista(edicao)
    print("\n\n**************REVISTA**************")
    print(revista.getColecao())
    


