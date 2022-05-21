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

#Exercício 3 - Lab3_IDLE_v2.pdf

def Repeticao_de_textos(texto, n):
    """Retorna n repetições do texto de entrada.
string, int -> string"""
    return (texto + " ") * n

#Exercício 4 - Lab3_IDLE_v2.pdf

def notacao_data (dia, mes, ano):
    """Com base no dia, mes e ano retorna a forma de notação padrão para data, dado por:
dia/mês/ano.
int, int, int -> string"""
    #segundo o calendário não existe valores de dia, mes e ano 0
    if((dia and mes and ano) > 0):
        return str(dia) + "/" + str(mes) + "/" + str(ano)
    return "Data não existente"

#Exercício 5 - Lab3_IDLE_v2.pdf

def funcao_exercicio (x):
    """retorna o valor de f(x) = y, para a função apresentada no exercício, que possui
diferentes formas para diferentes valores de x.
float -> float"""
    if(x < 0):
        return 0
    elif(0 <= x <=2):
        return x
    elif(2 < x <= 3.5):
        return 2
    elif(3.5 < x <= 5):
        return 3
    elif(x > 5):
        return (x**2) - (10*x) + 28
#Como temos uma função com 5 intervalos, e para cada intervalo um condicional diferente
#é necessario então no mínimo 5 testes, um no intervalo de cada condicional, para saber
#se a função funciona corretamente.

#Exercício 6 - Lab3_IDLE_v2.pdf

def Desconto_INSS(salario_bruto):
    """Com base no salário bruto, retorna o desconto percentual do INSS
float -> float
obs. o valor em real não deve possuir o simbolo R$, ex: R$150.00 = 150.00"""
    if(salario_bruto <= 0):
        return "situação inconsistente"
    
    if(salario_bruto <= 2000):
        return salario_bruto * (6/100)
    
    elif(2000 < salario_bruto <= 3000):
        return salario_bruto * (8/100)
    
    elif(salario_bruto > 3000):
        return salario_bruto * (10/100)

def Desconto_IR(salario_bruto):
    """Com base no salário bruto, retorna o desconto percentual do IR
float -> float
obs. o valor em real não deve possuir o simbolo R$, ex: R$150.00 = 150.00"""
    if(salario_bruto <= 0):
        return "situação inconsistente"
    
    elif(salario_bruto <= 2500):
        return salario_bruto * (11/100)
    
    elif(2500 < salario_bruto <= 5000):
        return salario_bruto * (15/100)
    
    elif(salario_bruto > 5000):
        return salario_bruto * (22/100)

def salario_liquido(salario_bruto):
    """Com base no valor do salário bruto, retorna o valor líquido da quantia, com os
descontos de IR, e do INSS.
float -> float
obs. o valor em real não deve possuir o simbolo R$, ex: R$150.00 = 150.00"""
    return salario_bruto - (Desconto_INSS(salario_bruto) + Desconto_IR(salario_bruto))


