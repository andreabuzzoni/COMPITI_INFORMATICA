# in un laboratorio di analisi i pazienti sono sottoposti ad esame
# secondo l'ordine di arrivo (usa una struttura di coda per memorizzare i nomi):
# scrivi il programma che registri i nomi dei pazienti man mano che arrivano.
# visualizza poi il primo paziente che deve essere sottoposto all'esame.

coda = []
paziente = ""

while paziente != "stop" :
 paziente = (input("inserire nome del paziente "))
 if paziente == "stop" :
          break
 coda.append(paziente)

print (coda[0])