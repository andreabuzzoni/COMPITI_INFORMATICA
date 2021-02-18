#Un'azienda vende prodotti in tutta Italia, e la rete di vendità è suddivisa in Nord, Centro, Sud, Isole. Dopo aver acquisito in un array il fatturato
#della quattro zone, calola: il totale del fatturato e i valori percentuali delle vendite nelle quattro zone rispetto al totale

zone={
    "nord":0,
    "centro":0,
    "sud":0,
    "isole":0 
}
fatturato_totale=0

for i in zone:
    while True:
            print("Inserire fatturato del", i)
            fatturato=int(input())
            break
    fatturato_totale+=fatturato
    zone[i]=fatturato

print("Il fatturato totale è", totale)