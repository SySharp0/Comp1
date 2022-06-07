#Lista_De_Atividades_3.py
#Raimundo José - OV/UFRJ - Comp 1
#raimundo.j.ferreira0@gmail.com

#Lista Lab4_MT - Exercício 1
def concatenacao (a, b):
    """Dado as strings de entrada a, b,  retorna a concateção das mesmas seguindo o
modelo "a+b+b+a".
string, string -> string"""
    if ((type(a) == str) and (type(b) == str)):
        return a + b + b + a
    return "O valor de entrada não é uma string"

#Lista Lab4_MT - Exercício 2
def substituo (s, x, i):
    """Com base em uma string s, troca o valor de index i pelo caractere x, retornando
então s com o valor do index i trocado por x.
string, string, int -> string"""
    if ((type(s) == str) and (type(x) == str) and (len(x) == 1) and (type(i) == int)
        and (0 <= i <= len(s))):
        fatia = s[0:i]
        sub = fatia + x
        return sub + s[i+1:]
    return "Os valores informados não condizem com o domínio da função"

#Lista Lab4_MT - Exercício 3
import math
def hashtag (s):
    """Com a string de entrada "s" essa função adicionará ao inicio, ao meio e no fim
da string o caractere "#", sendo que, para string com quantidade de elementos impares,
a aproximação da metade será feita para cima.
string -> string"""
    if(type(s) == str):
        metade = math.ceil(len(s)/2)
        return "#" + s[0: metade] + "#" + s[metade:] + "#"

#Lista Lab4_MT - Exercício 4

def filtra_pares (a):
    """ Recebendo obrigatóriamente uma tupla "a" contendo 4 algarismos inteiros de entrada
retorna uma nova tupla que filtrará e devolverá somente os valores de "a" que são pares.
tuple -> tuple"""
    if(len(a) == 4 and type(a) == tuple):
        pares = ()
        for elemento in a:
            if ((elemento % 2) == 0) or (elemento == 0):
                pares = pares + (elemento,)
        return pares
    return "Valores de entrada inválidos"

#Lista Lab4IDLE - Exercício 1

def SIGA (a):
    """ Recebe como entrada uma tupla "a" que deverá estar no formado (<nome_do_aluno>,
<nota1>, <nota2>, <nota2>) realiza o calculo de média das notas e retorna a situação final
do aluno, se for maior de 7 retornará aprovado e parabéns, caso esteja entre 5 e 7 retornará
aprovado, e por fim, caso esteja menor do que 5  retornará reprovado.
Obs. os valores retornados estarão com limitação de 2 casas decimais.
tuple -> tuple"""
    if (type(a) == tuple and len(a) == 4):        
        média = round(((a[1] + a[2] + a[3])/3),2)
        base = (a[0], média)
        if(média >= 7):
            return base + ("aprovado", "Parabéns")
        if(5 <= média < 7):
            return base + ("aprovado",)
        return base + ("reprovado",)
    return "Valores de entrada inválidos"

#Lista Lab4IDLE - Exercício 2

def signo_chines (mes):
    """ Com base no mes de nascimento da pessoa (valor de entrada), retorna em que ciclo
chinês a pessoa nasceu, e consequentemente o signo da pessoa.
int -> string"""
    signos_mes = ("Macaco", "Galo", "Cão", "Porco", "Rato", "Boi", "Tigre", "Coelho",
                  "Dragão", "Serpente", "Cavalo", "Carneiro")
    signo_da_pessoa = signos_mes[(mes % 12)]
    return signo_da_pessoa

#Lista Lab4IDLE - Exercício 3

def analise_de_numeros (telefone):
    """ Recebe como entrada um número de telefone em formato de string, então caso ele
seja válido retorna em 2 tuplas <(DDD), (Numero válido)>, caso seja invalido retorna então
2 tuplas vazias.
string -> tupla, tupla"""
    if(type(telefone) == str):
        if((len(telefone) == 8) and (telefone[0] == "3")):
            return (), (telefone,)
        if((len(telefone) == 9) and (telefone[0] == "9")):
            return (), (telefone,)
        if((len(telefone) == 10) and (telefone[2] == "3")):
            return (telefone[0:2]), (telefone[2:])
        if((len(telefone) == 11) and (telefone[2] == "9")):
            return (telefone[0:2]), (telefone[2:])
    return (),()

#Lista Lab4IDLE - Exercício 4

def formato_data(data):
    """ Recebe uma string de entrada, obrigatoriamente no padrão: <xx/xx/xx>, ou seja de 8
posições, na qual os valores de x devem ser numéricos e estarem no intervalo de 0 a 9.
Assim, retornará os tipos de notação de data válidos que aqueles números podem representar,
sendo que, caso não exista nenhuma notação de data aceitável, a função retornará uma tupla
vazia.
string -> tuple"""
    if (len(data) == 8):
        parte = [int(data[:2]), int(data[3:5]), int(data[6:])]
        if(0 < parte[1] <= 12) and (0 < parte[0] <= 12) and (0 < parte[2] <= 31):
            return ("dd/mm/yy","mm/dd/yy","yy/mm/dd")
        elif((0 < parte[1] <= 12) and (0 < parte[0] <= 31)) or ((0 < parte[0] <= 12) and (0 < parte[1] <= 31)):
            return ("dd/mm/yy","mm/dd/yy")
        elif(0 < parte[1] <= 12) and (0 < parte[2] <= 31):
            return("yy/mm/dd")
        return ()

#Lista Lab5IDLE - Exercício 1

def adicionar_contatinhosApp (nome, telefone = "vazio", email = "vazio", instagram = "vazio"):
    """ Recebe 4 parametros de entrada e os adiciona em uma lista conforma o padrão para
o aplicativo.
string, string, string, string -> list"""
    contato_novo = [nome, [telefone], email, instagram]
    return contato_novo

def atualizar_contatinhosApp (contato_antigo, índice, atualização):
    """ Reecbe como entrada um contato já adicionado, um índice (que representa qual informação
deseja acessar no sistema), e uma nova variável para atualizar o valor antigo(no determinado
índice).
Obs. caso os valores que serão alterados sejam os de nome, email ou instagram há uma substituição
da informação antiga por uma nova, descartando o que existia antes ali. Caso a informação
alterada seja o telefone háverá então o acrescimo da informação nova na lista(caso o aquele telefone
já não tenha sido adicionado), e por fim, caso seja passado um índice que não tenha
correspondência a função retorna a lista sem alterações.
list, int, str -> list"""
    if(0 <= índice <= 3):
        if(índice == 0) or (2 <= índice <= 3):
            contato_antigo[índice] = atualização
            return contato_antigo
        elif(índice == 1) and (atualização not in contato_antigo[índice]):
            if("vazio" not in contato_antigo[índice]):
                contato_antigo[índice] = contato_antigo[índice] + [atualização]
                return contato_antigo
            else:
                contato_antigo[índice][0] = atualização
                return contato_antigo
    return contato_antigo

#Lista Lab5IDLE - Exercício 2

def traducao_rnaM(trincas):
    """ Recebe 3 trincas de RNA e realiza a conversão dessas trincas para suas respectivas
representações em aminoácidos, retornando por fim a cadeia de aminoácidos correspondente as
tricas apresentadas.
str -> str"""
    aminoacidos = {"UUU" : "Phe", "CUU" : "Leu", "UUA" : "Leu", "AAG" : "Lisina", "UCU" :
                   "Ser", "UAU" : "Tyr", "CAA" : "Gln"}

    return  aminoacidos[trincas[:3]] + "-" + aminoacidos[trincas [3:6]] + "-" + aminoacidos[trincas[6:]]



            
            
                

            


        
        
