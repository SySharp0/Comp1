#Trabalho Final de Comp 1 - Jogo 2048
#Aplicação desenvolvida por Lois Valentim e Raimundo José

import random

tabuleiro = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
#Cada termo da lista indica uma linha da matriz, enquanto cada um dos valores
#representa uma casa

def vitoria(f_tab, c_vit):
    """Recebendo o tabuleiro no estado final do jogo (f_tab), e também um critério de
vitória, que deve ser o expoente da potência (c_vit) de base 2, cuja qual determinará o
grau de dificuldade do jogo, caso exista o valor da expressão (2**c_vit) no f_tab, essa
função retornará True, caso contrário, False.
matriz, int -> bool"""
    valor_de_vitoria = (2**c_vit)
    for linha in f_tab:
        for casa in linha:
            if(casa == valor_de_vitoria):
                return True
    return False

def dois_ou_quatro(tab):
    """ Adiciona os valores de 2 ou 4 em casas aleatórias do tabuleiro (tab) em uma posição
vazia, sendo que, a chande do valor aleatorio ser 2 é de 4/5 e de ser 4 é 1/5.
matriz -> none"""
    linha = random.randint(0,3)
    casa = random.randint(0,3)
    while(tab[linha][casa] != 0):
        linha = random.randint(0,3)
        casa = random.randint(0,3)
    if(tab[linha][casa] == 0):
        tab[linha][casa] = random.choice([2,2,4,2,2])
    return tab

def mostra_tabuleiro(tab):
    """Uma função que recebe uma matriz (que representa o tabuleiro) e realiza uma "impressão"
do mesmo na tela em formato de tabuleiro"""
    tabuleiro = []
    for linha in tab:
        for elemento in linha:
            tabuleiro = tabuleiro + [elemento]
    impressao = str(tabuleiro[:4]) + "\n" + str(tabuleiro[4:8]) + "\n" + str(tabuleiro [8:12]) + "\n" + str(tabuleiro[12:])
    print(impressao)

def direita(tab):
    """ Recebendo um tabuleiro realiza a movimentação do mesmo para a direita"""
    pode_ir = False
    somar = False
    rodar = 0
    repetir = 2
    
    for linha in tab:
        while(rodar < repetir):
            for a in range(0,4):
                #Etapas de verificação
                if(a != 3):
                    if(linha[a+1] == 0):
                        pode_ir = True
                    else:
                        pode_ir = False
                    if(linha[a+1] == linha[a]):
                        somar = True
                    else:
                        somar = False
                else:
                    pode_ir = False
                    somar = False

                #Realiza o movimento
                if(pode_ir == True):
                    linha[a+1] = linha[a]

                #Realiza a soma dos números caso eles sejam iguais
                if(somar == True):
                    linha[a+1] = linha[a] + linha[a+1]

                #Remove os 0
                if(pode_ir == True) or (somar == True):
                    linha[a] = 0

                #reinicia o for
                if(a == 3):
                    rodar = rodar + 1
        if(rodar == repetir):
            rodar = 0
    mostra_tabuleiro(tab)
            


    

    






