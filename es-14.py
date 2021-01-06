numeroA = int(input("scrivi il primo numero"))
numeroB = int(input("scrivi il secondo numero"))
prodotto = numeroA * numeroB
if prodotto > 10 :
    print ("il prodotto è maggiore di 10, la differenza è" , numeroA - numeroB)
elif prodotto < 10 :
    print ("il prodotto è minore di 10, la somma è" , numeroA + numeroB)
elif prodotto == 10 :
    print ("il prodotto è 10, la somma è" , numeroA + numeroB)