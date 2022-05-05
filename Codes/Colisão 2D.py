def colisão (x1,y1,x2,y2,xa,ya,xb,yb):
    """Detecta a colisão entre dois retângulos"""
    if((x2<xa) and (y2<ya)):
        return "Não houve colisão "
    return " Houve colisão "
