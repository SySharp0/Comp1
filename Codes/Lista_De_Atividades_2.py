#Lista_De_Atividades_2.py - Comp1 (IGA+IG1)
#Raimundo José Ferreira Filho - Astronomia
#Oservatório do Valongo - UFRJ

#Exercício 1 - Lab3_IDLE_v2.pdf

import math
def val_abs (x):
    """Calcula e retorna o valor absoluto de x.
int -> float
float -> float
Essa função não retorna o para números complexos pela impossibilidade da função math
em realizar operações algébricas com complexos."""
    #um número elevado ao quadrado sempre retornará seu módulo, segundo a matemática
    y = math.sqrt(x**2)
    return y
#Temos na matemática a definição de valor absoluto como sendo a distancia do valor para
#o ponto 0, ou seja, segue a forma de distância euclidiana, a função abs está habilitada
#a suportar qualquer valor, enquanto noça função limitada pelo múdulo math que não realiza
#operações com complexos não consegue receber esses valores.

#Exercício 2 - Lab3_IDLE_v2.pdf

def Delta_Discriminante(a,b,c):
    """Sendo o descriminante de uma função (delta) uma parte da função bhaskara, essa função retorna seu
valor algébrico com base nos coeficientes a, b, c da função.
float, float, float -> float"""
    return (b**2)-(4*a*c)

import math
def Raizes_da_função(a,b,c):
    """Com base nos valores dos coeficientes, a,b, c de um polinômio do segundo grau,
retorna suas raizes com (caso existam), com base no discrimante "delta".
float, float, float -> float"""
    delta = Delta_Discriminante(a,b,c)
    if(delta < 0):
        return "Não há raiz real"
    elif(delta == 0):
        # Segundo a matemática quando delta for 0 não importa terá somente uma raiz.
        return ((-b)+ math.sqrt(delta))/2*a
    elif(delta > 0):
        # Segundo a matemática para delta > 0 existe 2 raizes reais.
        return ((-b)+ math.sqrt(delta))/2*a , ((-b)- math.sqrt(delta))/2*a

