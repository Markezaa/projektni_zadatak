import sqlite3

conn = sqlite3.connect('Rent_a_car_baza.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS musterije_rent(
        id INTEGER PRIMARY KEY,
        ime TEXT,
        prezime TEXT,
        vozilo TEXT,
        dana INTEGER,
        naplaceno INTEGER
    )
''')

cursor.execute('''
    INSERT INTO musterije_rent (ime,prezime,vozilo,dana,naplaceno)
    VALUES ('Niko', 'Belic', 'Audi', 3, 240)
''')

cursor.execute('''
    INSERT INTO musterije_rent (ime,prezime,vozilo,dana,naplaceno)
    VALUES ('Ognjen', 'Djukic', 'BMW',10,1500)
''')
cursor.execute('''
    INSERT INTO musterije_rent (ime,prezime,vozilo,dana,naplaceno)
    VALUES ('Nemanja', 'Skolnik', 'Mercedes', 1, 70)
''')

conn.commit()

def izaberi_musterije():
    """Izaberi sve musterije iz tabele musterije_rent"""
    cursor.execute("SELECT * FROM musterije_rent")
    musterije=cursor.fetchall()
    return musterije

def prikazi_musterije(musterije):
    """Prikazi detalje o musterijama"""
    print("Musterije rent a cara:")
    for musterija in musterije:
        print(musterija)
    print()

def dodaj_musteriju():
    """Dodaj novu musteriju u tabelu musterije_rent"""
    ime=input("Unesite ime musterije:")
    prezime=input("Unesite prezime musterije:")
    vozilo=input("Unesite marku vozila:")
    dana=int(input("Unesite broj dana rentanja:"))
    naplaceno=int(input("Unesite naplacenu cijenu:"))

    cursor.execute("INSERT INTO musterije_rent(ime,prezime,vozilo,dana,naplaceno) VALUES (?,?,?,?)",
                   (ime,prezime,vozilo,dana,naplaceno))
    conn.commit()
    print("Musterija dodana na listu.")

while True:
    print("Izaberite akciju:")
    print("1. Prikazi sve musterije")
    print("2. Dodaj musteriju")
    print("0. Prekid programa")

    program = input("Unesite broj akcije:")

    if program == "1":
            musterije=izaberi_musterije()
            prikazi_musterije(musterije)


    elif program == "2":
        dodaj_musteriju()


    elif program == "3":
        print("Kraj programa!")
        break
    else:
        print("Program ne postoji. Izaberite program od 1-3!")
