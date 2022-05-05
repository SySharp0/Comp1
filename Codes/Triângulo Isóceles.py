def TrianguloIsoceles (l1,l2,l3):
    """ Retorna true caso os valores representem um triangulo isóceles"""
    return ((l1==l2) ^ (l2==l3) ^ (l3==l1)) ^ (l1==l2==l3)
