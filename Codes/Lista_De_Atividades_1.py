# Lista_De_Atividades_1.py
# Raimundo José Ferreira -  Comp1 - IGA+IG1
# raimundo22@ov.ufrj.com


#Lista 1 - Exercícios Extras - Exercício 1 -
def Conversão_de_moedas (valor_em_Real, taxa_de_Conversao = 4.94):
    """ Dado o "valor_em_Real" e uma "taxa_de_Conversão" realiza a conversão monetária,
sendo que, por questões de frequencia de uso, o valor default para a taxa de conversão
está definido como a cotação do dolar (4,94).
float, float=4.94 -> float"""
    return valor_em_Real / taxa_de_Conversao


#Lista 1 - Exercícios Extras - Exercício 2 -
def Valor_da_gorjeta (valor_da_conta, porcentagem_de_gorjeta):
    """Com base no valor da conta, retorna a porcentagem de gorjeta que deve ser paga.
OBS. o valor de "porcentagem_de_gorjeta" deve ser escrito sem o símbolo de porcentagem.
float, float -> float"""
    #Conversão da forma: x% para x/100
    taxa_de_gorjeta = porcentagem_de_gorjeta / 100
    return valor_da_conta * taxa_de_gorjeta


#Lista 1 - Exercícios Extras - Exercício 3 -
    # Exercicio 3.a)
    #COLOCAR PRINTS DOS VALORES DE TESTE
def Area_do_circulo(r):
    """Retorna o valor da área do círculo com base em seu raio r.
Por definição da questão temos que pi = 3.14.
float -> float"""
    pi = 3.14
    return pi * r**2

def Area_Coroa_Circular_a(r1, r2):
    """Calcula a área da coroa circular com base nos raios r1 e r2, referente aos dois
círculos. Na definição da questão temos que r1>r2 e que pi = 3.14.
float, float -> float"""
    return Area_do_circulo(r1) - Area_do_circulo(r2)


    # Exercicio 3.b)
from math import pi
    
def Area_do_circulo_b(r):
    """Retorna o valor da área do círculo com base em seu raio r. Sendo o valor de pi
importado da função math.
float -> float"""
    return pi * r**2

def Area_Coroa_Circular_b(r1, r2):
    """Calcula a área da coroa  circular com base nos raios r1 e r2, referente aos dois
círculos. Na definição da questão temos que r1>r2 e que o valor de pi será importado
da função math.pi.
float, float -> float"""
    return Area_do_circulo_b(r1) - Area_do_circulo_b(r2)


    # Exercicio 3.c)
def Erro_de_aproximação(r1,r2):
    """Com base nas funções acima descritas para os valores de pi=3.14 e o pi importado
da função math realiza a subtração entre os valores para encontrar a variação algébrica
entre o calculo aproximado e o preciso. Recebe como entrada 2 valores de raio.
float, float -> float"""
    return Area_Coroa_Circular_b(r1,r2) - Area_Coroa_Circular_a(r1,r2)


#Lista 2 - Lab1.pdf - Exercício 6 -
def Media_Ponderada(A, B):
        """Com base nos pares de valores inseridos, que condizem ao peso e ao valor algébrico
, retorna a média ponderada dos dois
algarismos de entrada.
tupla, tupla -> float"""
        return ((A[0]*A[1]) + (B[0]*B[1]))/ (A[0]+B[0])


#Lista 2 - Lab1.pdf - Exercício 7 -
def ProgressaoGeometrica(q):
    """Para uma P.G. com razão q entre 0<=q<1, define-se que a soma dos primeiros n termos
é suficiente para uma aproximaçãodo que seria a soma de todos os seus temos, já que o resultado
tenderá a 0, assim, essa funnção calcula com base na razão q o erro de aproximação entre a soma
infinita e a soma de n termos.
float -> float"""
    if(0<=q<1):
        soma_infinita = 1/(1-q)
        #Por meio de tentativas concui-se que os 7 primeiros termos são suficientes para uma aproximação considerável
        soma_n = (1*((q**7)-1))/(q-1)
        return soma_infinita - soma_n
    return "Valor de 'q' fora do domínio"


#Lista 2 - Lab1.pdf - Exercício 10 -
def Saldo_Final(Saldo_inicial, t_juros, meses):
    """Com base em uma conta bancária com saldo inicial, de uma taxa que deve ser declarada
na forma sem a porcentagem (ex. 5% = 5) e da quantidade em meses em que o juros mensal irá incidir
essa função calcula o saldo final da conta. Sendo que, os meses só contam para o calculo quando
representarem numeros fechados (naturais).
float, float, int -> float"""
    #Conversão da forma: x% para x/100
    taxa = t_juros/100
    t = int(meses)
    return Saldo_inicial * (1+ taxa * t)


#Lista 2 - Lab1.pdf - Exercício 11 -
def Correnteza_Barco(Velocidade_Correnteza, Largura_rio, Velocidade_barco):
    """Tendo os valores já determinados: velocidade da correnteza, largura do rio e velocidade do
barco, calcula a distância que a correnteza provoca no deslocamento do barco.
float, float, float -> float"""
    #Função proveniente da decomposição de vetores V(correnteza) e V(Barco), com base na função horária x(t) = x0 + v.t 
    return (Velocidade_Correnteza * Largura_rio) / Velocidade_barco


#Lista 3 - Lab2.pdf - Exercício 1 -
    # Exercicio 1.a)
def Teste():
    """Testa as funções max e min já definidas no módulo do Python, com base nos valores de entrada
oferecidos pela questão."""
    return max(3,2.8,3.9), min(7,2,4,1,0)

    # Exercicio 1.b)
def Media(a, b, c):
    """Calcula a média dos 3 valores inseridos.
float, float, float -> float"""
    return (a+b+c)/3

    # Exercicio 1.c)
def Comparacao_do_max(a, b, c):
    """Calcula a direfença entre o máximo valor dentre 3 algarismos e a média.
float, float, float -> float"""
    return max(a,b,c) - Media(a,b,c)

    # Exercicio 1.d)
def Soma_do_min(a, b, c):
    """Com base em 3 algarismos de entrada realiza a soma do menor valor dentre eles com a média.
float, float, float -> float"""
    return min(a, b, c) + Media(a,b,c)


#Lista 3 - Lab2.pdf - Exercício 2 -
    # Exercicio 2.a)
def Delta_Descriminante(a,b,c):
    """Sendo o descriminante de uma função (delta) uma parte da função bhaskara, essa função retorna seu
valor algébrico com base nos coeficientes a, b, c da função.
float, float, float -> float"""
    return (b**2)-(4*a*c)

    # Exercicio 2.b)
def Primeira_Raiz (a,b,c):
    """Com base na função acima descrita para o calculo de delta(Delta_Descriminante()), e nos coeficientes
de um polinômio do segundo grau a,b,c, retorna o valor da primeira raiz do polinômio.
float, float, float -> float"""
    import math
    if(Delta_Descriminante(a,b,c)>0):
        return ((-b)+ math.sqrt(Delta_Descriminante(a,b,c)))/2*a
    return "Raiz não existe no dominio da função"

    # Exercicio 2.c)
def Segunda_Raiz (a,b,c):
    """Com base na função acima descrita para o calculo de delta (Delta_Descriminante()), e nos coeficientes
de um polinômio do segundo grau a,b,c, retorna o valor da segunda raiz do polinômio.
float, float, float -> float"""
    import math
    if(Delta_Descriminante(a,b,c)>0):
        return ((-b)- math.sqrt(Delta_Descriminante(a,b,c)))/2*a
    return "Raiz não existe no dominio da função"


#Lista 3 - Lab2.pdf - Exercício 3 -
    # Exercicio 3.a)
def Numero_de_Termos(a1, an, r):
    """Com base na definição de uma PA, que é dada pela formula: an=a1+nr-n, retorna o valor de n, ou seja,
o numero de termos da PA, por meio de uma manipulação da equação supracitada.
float, float, float -> float"""
    return (an-a1+r)/r

    # Exercicio 3.b)
def Soma_PA(a1, an, r):
    """Com bases nos valores que serão inseridos: primeiro termo (a1), do ultimo termo (an), e da razão da PA (r)
retorna a o valor da soma da PA, com base no valor do numero de termos obtidos por meio da função anteriormente
descrita (Numero_de_Termos()). 
float, float, float -> float"""
    n = Numero_de_Termos(a1,an,r)
    return (n*(a1+an))/2


#Lista 3 - Lab2.pdf - Exercício 4 -
import math
    # Exercicio 4.a)
def Distancia_2_Pontos(A,B):
    """Calcula a distancia entre dois pontos, dado suas cordenadas (ax,ay) em um eixo cartesiano, por meio da 
formula Euclidiana para distância.
tupla, tupla -> float"""
    return math.dist(A,B)

    # Exercicio 4.a)
def Perimetro_Cateto():
    """"""
    return 




    
