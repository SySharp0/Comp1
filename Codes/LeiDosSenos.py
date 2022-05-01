import math

#AnguloB
#AnguloC
#LadoAC

def LeiDosSenos (LadoAC, AnguloB, AnguloC):
    """ retorna aproximadamente os valores do lado AB, e BC de um triangulo utilizando a Lei dos Senos,
com base nos valores do LadoAC do angulo B e C"""
    
    AnguloA = 180-AnguloB-AnguloC
    
    A = math.radians(AnguloA)
    B = math.radians(AnguloB)
    C = math.radians(AnguloC)
    
    LadoAB = (LadoAC * math.sin(C))/math.sin(B)
    LadoBC = (LadoAC * math.sin(A)/math.sin(B))
    return round(LadoAB, 1) , round(LadoBC, 1)
