#Lista de atividades 4 - Comp 1 OV1
#Raimundo José Ferreira Filho - Astronomia
#raimundo22@ov.ufrj.br

#Lista - exercício 1 -

def intercalando_listas(l1, l2):
    """ Dado 2 listas como entrada, retorna uma terceira lista com os valores intercalados
da primeira, com a segunda, ou seja, se a primeira lista for [a,a,a] e a segunda [b,b,b], a
terceira lista será [a,b,a,b,a,b].
list, list -> list"""
    l3 = ["a","b","c","d","e","f"]
    i = 0
    j = 0
    while (i < 3) and (j < 6):
        l3[j] = l1[i]
        j=j+1
        l3[j] = l2[i]
        j=j+1
        i=i+1
    return l3

#Lista - exercício 1 -

def pontos_por_time (jogos):
    """ """
    jogo_ida = jogos[:1]
    jogo_volta = jogos[1:]
    pontos_1 = 0
    pontos_2 = 0
    if(jogo_ida[2] > jogo_ida[2]):
        pontos_1 = pontos_1 + 3
    if(jogo_ida[2] > jogo_ida[2]):
        pontos_1 = pontos_1 + 1
        pontos_1 = pontos_1 + 1
        
 #   tabela = {(jogo_ida[0]) : , jogo_ida[1]}
    return tabela
    
