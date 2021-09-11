import edicao as ed
import artigo as ar
import autor  as au
import avaliador  as av
import revista  as re
import auxiliar as aux
artigos=[]
artigosReprovados=[]
artigosAprovados=[]
avaliadores=[]
autores=[]

avaliadores=aux.inserirAvaliadores()                                #OK    
autores=aux.inserirAutores()                                        #OK
artigos=aux.inserirArtigos(autores)                                 #OK
#for c in range(0,len(artigos)): print(artigos[c].dadosArtigo())

