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


avaliadores=aux.inserirAvaliadores()                                   
autores=aux.inserirAutores()                                        
artigos=aux.inserirArtigos(autores)                                       
edicao=aux.inserirEdicao(artigos)
                                     
for c in range(0,len(artigos)):
    re.AvaliarArtigo(artigos[c],avaliadores) 
    if(artigos[c].getNota()>=7): artigosAprovados.append(artigos[c])


#for c in range(0,len(artigos)): print(artigos[c].dadosArtigo())

