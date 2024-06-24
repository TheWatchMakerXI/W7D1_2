import string #per usare le funzione generatrici della libreria in questo caso
import random #per la creazione casuale

def genera_password(tipo='scelta'):
    if tipo == 'semplice':
        caratteri = string.ascii_letters + string.digits
        lunghezza = 8
    elif tipo == 'complicata':
        caratteri = string.ascii_letters + string.digits + string.punctuation
        lunghezza = 20
    else:
        #raise per stoppare il programma con un messaggio di errore
        raise ValueError("Tipo di password non valido. Scegli 'semplice' o 'complicata'.")
    
    password = ''.join(random.choice(caratteri) for _ in range(lunghezza))#la funziona join serve per concatenare gli elementi in una lista, quella random per generarmi alcuni dall'insieme a lui assegnato in questo caso
    return password 


scelta=input("Scegli la tipologia di password, semplice(senza simboli) o complicata(anche con simboli):")
password_generata = genera_password(scelta)
if (scelta== 'semplice'):
    print(f"\nPassword semplice generata e': {password_generata}\n\n ")
else:
    print(f"\nPassword complicata generata e': {password_generata}\n\n ")
