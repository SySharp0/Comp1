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

#Lista - exercício 2 -

def pontos_por_time (resultados):
    """ Recebe como entrada uma lista, contendo duas listas secundarias, sendo que, cada
lista secundária deve seguir a estrutura: [["time1", "time2"], [numero_de_gols_time1,
numero_de_gols_time2]], assim, essa função retornará a pontuação feita na rodada por cada
um dos times, usando a máxima de que a vitória concede 3 pontos, o empate 1, e a derrota 0
lista -> dicionario"""
    #primeiro jogo
    if(type(resultados) == list):
        resultados1 = [0 , 0]
        if(resultados[0][1][0] > resultados[0][1][1]):
            resultados1[0] = resultados1[0] + 3
        elif(resultados[0][1][0] == resultados[0][1][1]):
            resultados1[0] = resultados1[0] + 1
            resultados1[1] = resultados1[1] + 1
        elif(resultados[0][1][1] > resultados[0][0][0]):
            resultado[1] = resultado[1] + 3
            
    #segundo jogo
        if(resultados[1][1][0] > resultados[1][1][1]):
            resultados1[1] = resultados1[1] + 3
        elif(resultados[1][1][0] == resultados[1][1][1]):
            resultados1[0] = resultados1[0] + 1
            resultados1[1] = resultados1[1] + 1
        elif(resultados[1][1][1] > resultados[1][0][0]):
            resultado[0] = resultado[0] + 3

    #dicionário
        final = {resultados[0][0][0]: resultados1[0], resultados[0][0][1]: resultados1[1]}
        return final
    return "O parametro deve ser uma lista!"

#Lista - exercício 3 -

def sera_que_um_colchao_passa_pela_porta (dimensoes, altura_porta, largura_porta):
    """ Sendo A o comprimento, B a largura e C a altura de um colchão, que deverão ser
passados na forma de uma lista [A, B, C], e a altura e a largura de uma porta (todos os
valores em centímetros), retorna se será possivel passar o colchão pela porta.
lista, inteiro, inteiro -> booleano """
    #caso A esteja paralelo ao chão
    if(dimensoes[1] < altura_porta and dimensoes[2] < largura_porta):
        return True

    #caso B esteja paralelo ao chão
    if(dimensoes[1] < largura_porta and dimensoes[2] < altura_porta):
        return True
    
    #caso C esteja paralelo ao chão
    if(dimensoes[0] < largura_porta and dimensoes[1] < altura_porta):
        return True
    return False
    
#Lista - exercício 1 -
def deletar_contatinho(contatinho, telefone_deletar):
    """ Recebe as informações de contato em uma lista, que devem seguir a estrutura :
["nome", ["lista de telefones"], "email", "instagram"] em que todos os valores devem
estar na forma de string e a lista de telefones deve ser uma lista, e deletao termo
"telefone_deletar" caso ele esteja na lista"""
    for informacao in contatinho:
        if(type(informacao) == list):
            for telefones in informacao:
                if(telefones == telefone_deletar):
                    list.remove(informacao, telefone_deletar)
                    return True
    return False

#Lista - exercício 2 -
def campeonato (tabela):
    """ Recebe como entrada uma tabela que deverá ser apresentada como uma matriz, ou seja
uma lista (colunas) de listas(linhas), que obrigatoriamente deve contar na primeira coluna
o nome dos times em formato de string, e na segunda a pontuação de cada um deles que deve
ser um valor inteiro, e retorna os nomes dos times do campeonato, a pontuação do time
campeão e a média de pontos do campeonato.
matriz -> list, int, float"""
    lista_de_times = []
    pontuacoes = []
    somar = 0
    for time in tabela:
        for var in time:
            if(type(var) == str):
                list.append(lista_de_times, var)
            if(type(var) == int):
                list.append(pontuacoes, var)
    for valor in pontuacoes:
        somar = somar + valor
    media = somar / len(pontuacoes)
    return lista_de_times, max(pontuacoes), media
                
            


