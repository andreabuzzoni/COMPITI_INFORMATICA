#crea un programma che verifichi se una parola data in input è palindroma
parola1 = input("scrivi una parola")
parola2 = parola1[::-1]
if parola1 == parola2:
   print ("parola palindroma")
else:
   print ("parola non palindroma")
