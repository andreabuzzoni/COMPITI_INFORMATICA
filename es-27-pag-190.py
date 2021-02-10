#Organizza con un dizionario la rubrica con i nomi delle persone e i rispettivi numeri telefonici. 
#Fornito poi il nome della persona, il programma visualizza il suo numero di telefono 
#oppure un messaggio nel caso la persona non sia presente nella rubrica.

nomi_numeri={
    "giuseppe":"339 375424",
    "segreteria ufficio":"0552 12746",
    "susanna":"347 627934"
}

while True:
    contatto=input("Inserire il nome della persona della quale si vuole cercare (per fermare inserire stop) ")
    if contatto=="stop":
        break
    if contatto in nomi_numeri:
        print("Il numero di", contatto, "è", nomi_numeri[contatto])
    else:
        print("Contatto non trovato")
        aggiunta=input("Si vuole aggiungere il contatto? ")
        if aggiunta=="si":
            print("Inserire il numero di", contatto)
            numero=input()
            nomi_numeri[contatto]=numero
            print("Numero aggiunto correttamente\n\n"
        else :
            print ("il contatto non è stato aggiunto")