L_quadrato = int(input("lato del quadrato:\n"))
A_quadrato = L_quadrato ** 2
print ("l'area è " , A_quadrato)

B_rettangolo = int(input("base del rettangolo:\n"))
H_rettangolo = int(input("area del rettangolo:\n"))
A_rettangolo = B_rettangolo * H_rettangolo
print ("l'area è" , A_rettangolo)

B_triangolo = int(input("base del triangolo:\n"))
H_triangolo = int(input("altezza del triangolo:\n"))
A_triangolo = (B_triangolo * H_triangolo) / 2
print ("l'area è" , A_triangolo)

R_cerchio = int(input("raggio del cerchio:\n"))
A_cerchio = R_cerchio ** 2 * 3.14
print ("l'area è" , A_cerchio) 

RISULTATI = [A_quadrato , A_rettangolo , A_triangolo , A_cerchio]
print ("l'area maggiore è" , (max(RISULTATI)))
