def colisão (x1,y1,x2,y2,xa,ya,xb,yb):
    """Detecta a colisão entre dois retângulos"""
    if((x2<xa) or (y2<ya) or (x1>xb) or (y1>yb)):
        return "Não houve colisão"
    return " Houve colisão"
