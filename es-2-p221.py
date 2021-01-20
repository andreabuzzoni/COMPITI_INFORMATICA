#Calcola il vertice e il fuoco di una parabola 

def delta (a, b,c):
    val_delta = b**2-(4*a*c)
    return val_delta

def vertice (a, b, c):
    val_delta = delta(a, b ,c)
    x_vertice = -b/(2*a)
    y_vertice = -val_delta/(4*a)
    return x_vertice, y_vertice

def fuoco (a, b, c):
    val_delta = delta(a, b, c)
    x_fuoco = -b/(2*a)
    y_fuoco = -(1-val_delta)/(4*a)
    return x_fuoco, y_fuoco

while True:
    try:
        valore_a=float(input("Inserisci a "))
        valore_b=float(input("Inserisci b "))
        valore_c=float(input("Inserisci c "))
    except ValueError:
        print("Il valore non è valido")
        continue
    break
c_vertice = vertice(valore_a, valore_b, valore_c)
c_fuoco = fuoco(valore_a, valore_b, valore_c)

print("Il vertice ha coordinate",c_vertice,"\nIl fuoco ha coordinate", c_fuoco)