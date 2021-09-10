import edicao as ed
import artigo as ar
import autor  as au
import avaliador  as av
import revista  as re

#teste para ver se ta OK com as classes***************  TUDO OK
av1=av.Avaliador('alexandre','user1@gmail.com','Tecnologia')
av2=av.Avaliador('maiure','user2@gmail.com','Tecnologia')
av3=av.Avaliador('ana','user3@gmail.com','Tecnologia')
aut1=au.Autor('joselito','userAutor@gmail.com','IFBA','Camaçari')
art1=ar.Artigo(aut1,'Mineração de dados','arquivo')
art2=ar.Artigo(aut1,'Big datas','arquivo')
art3=ar.Artigo(aut1,'Segurança da informação','arquivo')
art4=ar.Artigo(aut1,'Banco de dados','arquivo')
art5=ar.Artigo(aut1,'Titulo','arquivo')
""" av1.dadosAvaliador()
print('\n')
av2.dadosAvaliador()
print('\n')
av3.dadosAvaliador()
print('\n')
aut1.dadosAutor()
print('\n')
art1.dadosArtigo()
print('\n')
art2.dadosArtigo()
print('\n')
art3.dadosArtigo()
print('\n')
art4.dadosArtigo()
print('\n')
art5.dadosArtigo() """

#Dando Nota para Artigo***********************          TUDO OK
""" art1.dadosArtigo()
print('\n')
analise=re.AvaliarArtigo(art1,av1,av2,av3)
print('\n')
art1.dadosArtigo() """

