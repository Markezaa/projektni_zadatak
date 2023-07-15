import sqlite3

conn=sqlite3.connect('Rent_a_car_baza.db')
cursor=conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS vozila_dolaze(
        id INTEGER PRIMARY KEY,
        marka TEXT,
        model TEXT,
        godiste INTEGER,
        placeno INTEGER,
        zemlja TEXT,
        tip TEXT
    )
''')

cursor.execute('''
    INSERT INTO vozila_dolaze (marka,model,godiste,placeno,zemlja,tip)
    VALUES ('Volkswagen','Passat',2013,11000,'Belgija','Prodaja')
''')

cursor.execute('''
    INSERT INTO vozila_dolaze (marka,model,godiste,placeno,zemlja,tip)
    VALUES ('Peugeot','508',2021,65000,'Belgija','Rent')
''')


cursor.execute('''
    INSERT INTO vozila_dolaze (marka,model,godiste,placeno,zemlja,tip)
    VALUES ('Audi','A6',2019,89000,'Svajcarska','Rent')
''')
conn.commit()

def izaberi_vozilo():
    """Izaberi sva vozila iz tabele vozila_dolaze"""
    cursor.execute("SELECT * FROM vozila_dolaze")
    vozila=cursor.fetchall()
    return vozila

def prikazi_vozila_u_dolasku(vozila):
    """Prikazi detalje o vozilima u dolasku"""
    print("Vozila u dolasku:")
    for vozilo in vozila:
        print(vozilo)
    print()

def dodaj_novo_vozilo():
    """Dodaj novo vozilo u tabelu vozila_dolaze"""
    marka=input("Unesite marku vozila")
    model = input("Unesite model vozila:")
    godiste = int(input("Unesite godiste vozila:"))
    placeno = int(input("Unesite cijenu u KM:"))
    zemlja = input("Unesite zemlju kupovine:")
    tip=input("Unesite tip poslovanja sa vozilom:")

    cursor.execute("INSERT INTO vozila_dolaze(marka,model,godiste,placeno,zemlja,tip) VALUES (?,?,?,?,?,?)",
                   (marka,model,godiste,placeno,zemlja,tip))
    conn.commit()
    print("Novo vozilo je dodano")

def obrisi_vozilo(id_vozila):
    """Obrisi vozilo sa datim ID iz tabele lista_vozila."""
    cursor.execute("DELETE FROM vozila_dolaze WHERE id=?", (id_vozila))
    conn.commit()

while True:
    while True:
        print("Izaberite program:")
        print("1. Prikazi sva vozila za prodaju")
        print("2. Dodaj vozilo za prodaju")
        print("3. Obrisi vozilo sa liste")
        print("0. Prekid programa")

        program=input("Unesite broj programa")

        if program=="1":
            vozila=izaberi_vozilo()
            prikazi_vozila_u_dolasku(vozila)

        elif program=="2":
            dodaj_novo_vozilo()

        elif program== "3":
            vozila = izaberi_vozilo()
            prikazi_vozila_u_dolasku(vozila)
            id_vozila = input("Unesite ID vozila koje zelite da obrisete")
            obrisi_vozilo(id_vozila)
            print("Vozilo uspjesno obrisano sa liste")

        elif program == "0":
            print("KRAJ PROGRAMA!!!")
            break

        else:
            print("Program ne postoji. Izaberite program od 0-3!")


