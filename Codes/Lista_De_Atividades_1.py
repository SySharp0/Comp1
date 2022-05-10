# Lista_De_Atividades_1.py
# Raimundo José Ferreira -  Comp1 - IGA+IG1

#Lista 1 - Exercícios Extras - Exercício 1 -
def Conversão_de_moedas (valor_em_Real, taxa_de_Conversao = 4.94):
    """ Dado o "valor_em_Real" e uma "taxa_de_Conversão" realiza a conversão monetária,
sendo que, por questões de frequencia de uso, o valor default para a taxa de conversão
está definido como a cotação do dolar (4,94)"""
    return valor_em_Real / taxa_de_Conversao

#Lista 1 - Exercícios Extras - Exercício 2 -
def Valor_da_gorjeta (valor_da_conta, porcentagem_de_gorjeta):
    """Com base no valor da conta, retorna a porcentagem de gorjeta que deve ser paga.
OBS. o valor de "porcentagem_de_gorjeta" deve ser escrito sem o símbolo de porcentagem"""
    #Conversão da forma: x% para x/100
    taxa_de_gorjeta = porcentagem_de_gorjeta / 100
    return valor_da_conta * taxa_de_gorjeta

#Lista 1 - Exercícios Extras - Exercício 3 -
    # Exercicio 3.a)
    #COLOCAR PRINTS DOS VALORES DE TESTE
def Area_do_circulo(r):
    """Retorna o valor da área do círculo com base em seu raio r.
Por definição da questão temos que pi = 3.14"""
    pi = 3.14
    return pi * r**2
def Area_Coroa_Cicular_a(r1, r2):
    """Calcula a área da coroa  circular com base nos raios r1 e r2, referente aos dois
círculos. Na definição da questão temos que r1>r2 e que pi = 3.14"""
    return Area_do_circulo(r1) - Area_do_circulo(r2)
    # Exercicio 3.b)
    def Area_do_circulo(r):
    """Retorna o valor da área do círculo com base em seu raio r.
Por definição da questão temos que pi = 3.14"""
    pi = 3.14
    return pi * r**2
def Area_Coroa_Cicular_b(r1, r2):
    """Calcula a área da coroa  circular com base nos raios r1 e r2, referente aos dois
círculos. Na definição da questão temos que r1>r2 e que o valor de pi será importado
da função math.pi"""
    from math import pi
    return 





