#elenca proprietà e metodi della classe Prodotto

class Prodotto:
    def __init__(self, nome, prezzo):
        self.nome = nome
        self.prezzo = prezzo
    
    def assegna_prezzo(self):
        self.prezzo = self.prezzo * self.numero

    def informazioni(self):
        print("il costo di ", self.nome, "è", self.prezzo, "€")

    prodotto_1 = ("jeans", 2, 49)
    prodotto_1.assegna_prezzo()
    prodotto_1.informazioni()

    prodotto_2 = ("felpa", 1, 29)
    prodotto_2.assegna_prezzo()
    prodotto_2.informazioni()