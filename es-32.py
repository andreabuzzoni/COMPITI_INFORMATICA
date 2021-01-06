#calcola il valore di un'equazione in base alle variabili
numeroA = int(input("scrivi il valore di A"))
numeroB = int(input("scrivi il valore di B"))
if numeroA == 0 and numeroB == 0 :
    print ("l'equazione è indeterminata")
elif numeroA != 0 and numeroB == 0 :
    print ("il risultato è x = 0")
elif numeroA == 0 and numeroB != 0 :
    print ("l'equazione è impossibile")
elif numeroA != 0 and numeroB != 0 :
    print ("la soluzione dell'equzione è - B / A")