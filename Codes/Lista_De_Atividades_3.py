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
