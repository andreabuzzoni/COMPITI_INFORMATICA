#Creare una classe Atleta per rappresentare le informazioni su un giocatore. 
#La classe deve contenere un attributo booleano chiamato visita_medica.
#Deve contenere un metodo per assegnare all'atleta il nome della squadra dove gioca.
#Aggiungere alla classe Atleta un metodo chiamato effettua_visita che ponga l'attributo visita_medica uguale a True.
#Aggiungere alla classe un metodo per visuallizare i dati del giocatore.

class Atleta:
     def __init__(self , nome , cognome , anni , squadra = "sconosciuta" , visita_medica = False) :
         self.nome = nome
         self.cognome = cognome
         self.anni = anni
         self.squadra = squadra
         self.visita_medica = visita_medica

     def informazioni(self) :
         print("Nome: {}Cognome: {}Età: {}Squadra: {}Deve effettuare una visita medica: {}\
         ".format(self.nome, self.cognome, self.anni, self.squadra, self.visita_medica))

     def aggiunta_squadra(self, nome_squadra):
         self.squadra = nome_squadra

     def effettua_visita(self) :
         self.visita_medica = True

 a1 = Atleta("Paolo", "Verdi", 17)
 a1.informazioni()
 a1.aaggiunta_squadra("Reggiana")
 a1.effettua_visita()
 a1.informazioni()
