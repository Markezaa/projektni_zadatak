import sqlite3

conn=sqlite3.connect('Rent_a_car_baza.db')

cursor=conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS lista_vozila (
        id INTEGER PRIMARY KEY,
        marka TEXT,
        model TEXT,
        godiste INTEGER,
        gorivo TEXT,
        kilometraza INTEGER,
        cijena_dan INTEGER
    )
''')

cursor.execute('''
    INSERT INTO lista_vozila (marka,model,godiste,gorivo,kilometraza,cijena_dan)
    VALUES( 'Audi','A5',2015,'Dizel',128000,80)
    ''')

cursor.execute('''
        INSERT INTO lista_vozila (marka,model,godiste,gorivo,kilometraza,cijena_dan)
    VALUES ('Mercedes Benz','E250', 2012,'Dizel',200000,70)
    ''')
cursor.execute('''
        INSERT INTO lista_vozila (marka,model,godiste,gorivo,kilometraza,cijena_dan)
    VALUES ('BMW','760Li',2018,'benzin',24000,150)
    ''')

def izaberi_vozilo():
    """Izaberi sva vozila iz tabele lista_vozila"""
    cursor.execute("SELECT * FROM lista_vozila")
    vozila=cursor.fetchall()
    return vozila

def azuriraj_kilometrazu_vozila(id_vozila,trenutna_kilometraza):
    """Azuriraj kilometrazu vozila sa ID-jem."""
    cursor.execute("UPDATE lista_vozila SET kilometraza=? WHERE id=?",(trenutna_kilometraza,id_vozila))
    conn.commit()

def obrisi_vozilo(id_vozila):
    """Obrisi vozilo sa datim ID iz tabele lista_vozila."""
    cursor.execute("DELETE FROM lista_vozila WHERE id=?", (id_vozila))
    conn.commit()
    print("Vozilo uspjesno obrisano!")

def prikazi_sva_vozila(vozila):
    """Prikazi detalje o vozilima."""
    print("Vozila:")
    for vozilo in vozila:
        print(vozilo)
    print()


while True:
    print("Izaberite akciju:")
    print("1. Prikazi sva vozila")
    print("2. Azuriraj kilometrazu vozila")
    print("3. Obrisi vozilo sa liste")
    print("0. Prekid programa")

    program=input("Unesite broj akcije:")

    if program=="1":
        vozila=izaberi_vozilo()
        prikazi_sva_vozila(vozila)

    elif program =="2":
        vozila = izaberi_vozilo()
        prikazi_sva_vozila(vozila)

        id_vozila=input("Unesite ID vozila:")
        trenutna_kilometraza=int(input("Unesite novu kilometrazu"))
        azuriraj_kilometrazu_vozila(id_vozila, trenutna_kilometraza)
        print('Kilometraza vozila uspjesno azurirana.')
        vozila= izaberi_vozilo()
        prikazi_sva_vozila(vozila)

    elif program =="3":
        vozila = izaberi_vozilo()
        prikazi_sva_vozila(vozila)

        id_vozila=input("Unesite ID vozila koje zelite obrisati sa liste:")
        obrisi_vozilo(id_vozila)
        print("Vozilo obrisano!")

        vozila = izaberi_vozilo()
        prikazi_sva_vozila(vozila)

    elif program ==("0"):
        print('KRAJ PROGRAMA!')
        break

    else:
        print("Program ne postoji. Izaberite program od 0-3!")