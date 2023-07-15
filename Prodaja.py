import sqlite3

conn = sqlite3.connect('Rent_a_car_baza.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS prodaja_vozila (
        id INTEGER PRIMARY KEY,
        marka TEXT,
        model TEXT,
        godiste INTEGER,
        snaga INTEGER,
        cijena INTEGER
    )
''')

cursor.execute('''
    INSERT INTO prodaja_vozila (marka,model,godiste,snaga,cijena)
    VALUES ('Audi','s8',2017,605,155000)
''')
cursor.execute('''
    INSERT INTO prodaja_vozila (marka,model,godiste,snaga,cijena)
    VALUES ('Fiat','Punto_Evo',2012,70,8990)
''')
cursor.execute('''
    INSERT INTO prodaja_vozila (marka,model,godiste,snaga,cijena)
    VALUES ('Volkswagen','Golf',2014,150,19500)
''')
cursor.execute('''
    INSERT INTO prodaja_vozila (marka,model,godiste,snaga,cijena)
    VALUES ('Skoda','Octavia',2016,185,31500)
''')

def izaberi_prodaja_vozila():
    """Izaberi sva vozila za prodaju"""
    cursor.execute("SELECT * FROM prodaja_vozila")
    prodaj=cursor.fetchall()
    return prodaj

def prikazi_prodaju_vozila(prodaja):
    """Prikazi detalje o prodaji vozila"""
    print("Prodaja vozila:")
    for prodaje in prodaja:
        print(prodaje)
    print()

def dodaj_vozila_za_prodaju():
    """Dodaj nova vozila na listu za prodaju u tabeli prodaja_vozila"""
    marka=input("Unesite marku vozila:")
    model=input("Unesite model vozila:")
    godiste=int(input("Unesite godiste vozila:"))
    snaga=int(input("Unesite snagu u KS:"))
    cijena= int(input("Unesite cijenu u KM:"))

    cursor.execute("INSERT INTO prodaja_vozila (marka,model,godiste,snaga,cijena)"
                   "VALUES (?,?,?,?,?)", (marka,model,godiste,snaga,cijena))
    conn.commit()
    print("Vozilo uspjesno dodano na listu za prodaju.")

def obrisi_vozilo(id_vozila):
    """Izbrisi vozilo sa liste prodaja_vozila"""
    cursor.execute("DELETE FROM prodaja_vozila WHERE id=?",(id_vozila,))
    conn.commit()
    print("Vozilo uspjesno obrisano sa liste")

while True:
    while True:
        print("Izaberite akciju:")
        print("1. Prikazi sva vozila za prodaju")
        print("2. Dodaj vozilo za prodaju")
        print("3. Obrisi vozilo sa liste")
        print("0. Prekid programa")

        program = input("Unesite broj akcije:")

        if program =="1":
            prodaja=izaberi_prodaja_vozila()
            prikazi_prodaju_vozila(prodaja)

        elif program =="2":
            dodaj_vozila_za_prodaju()

        elif program =="3":
            prodaja=izaberi_prodaja_vozila()
            prikazi_prodaju_vozila(prodaja)

            id_vozila = int(input("Unesite ID vozila koje zelite da obrisete"))

            obrisi_vozilo(id_vozila)
            print("Vozilo uspjesno obrisano sa liste")

        elif program =="0":
            print("KRAJ PROGRAMA!!!")
            break

        else:
             print("Program ne postoji. Izaberite program od 0-3!")



