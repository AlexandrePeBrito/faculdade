#originalidade, conteúdo e apresentação
from random import randint

def AvaliarArtigo(artigo,avaliador1,avaliador2,avaliador3):
    print(f"Os avaliadores do Artigo {artigo.getNome()} sao: ")
    avaliador1.dadosAvaliador()
    avaliador2.dadosAvaliador()
    avaliador3.dadosAvaliador()
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
            print('Media final em Originalidade: {originalidade}')

        elif c==1: 
            print(f'\nEm conteudo os avaliadores deram a seguintes notas:\n'+
            f'Avaliador1 {avaliador1.getNome()} : {notaAvaliador1}\n'+
            f'Avaliador2 {avaliador2.getNome()} : {notaAvaliador2}\n'+
            f'Avaliador3 {avaliador3.getNome()} : {notaAvaliador3}\n')
            conteudo=(notaAvaliador1+notaAvaliador2+notaAvaliador3)/3
            print('Media final em Conteudo: {conteudo}')

        elif c==2: 
            print(f'\nEm apresentação os avaliadores deram a seguintes notas:\n'+
            f'Avaliador1 {avaliador1.getNome()} : {notaAvaliador1}\n'+
            f'Avaliador2 {avaliador2.getNome()} : {notaAvaliador2}\n'+
            f'Avaliador3 {avaliador3.getNome()} : {notaAvaliador3}\n')
            apresentação=(notaAvaliador1+notaAvaliador2+notaAvaliador3)/3
            print('Media final em Apresentação: {apresentação}')
    nota=(originalidade+conteudo+apresentação)/3
    print('Nota final do Artigo: {nota}')
    artigo.setNota(nota)
