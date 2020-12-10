N_parole = int(input('quante parole vuoi analizzare?'))
A = []
B = []
contatore = 1
while True: 
    parola = input('inserire la parola:')
    A.append(parola)
    B.append(len(parola))
    if N_parole == contatore :
        print('il n. di lettere è', B)
        break
    contatore = contatore + 1
