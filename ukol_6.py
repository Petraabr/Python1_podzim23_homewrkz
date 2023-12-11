class Auto:

    def __init__(self, registracni_znacka, typ_vozidla, najete_km):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.vypujceno = True

    def pujc_auto(self):
        if self.vypujceno:
            self.vypujceno = False
            return ("Vozidlo bylo vypůjčeno.")
        else:
            return("Vozidlo je nedostupné.")

    def get_info(self):
        return (f"Registrační značka auta: {self.registracni_znacka}.")


prvni_auto = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
druhe_auto = Auto("1P3 4747", "Škoda Octavia", 41253)



typ_vozidla = input("Které auo si chcete vypůjčit: ")
print(typ_vozidla)
    

if typ_vozidla == "Peugeot":
    print(prvni_auto.get_info())
    print(prvni_auto.pujc_auto())
    
    
if typ_vozidla == "Škoda":
    print(druhe_auto.get_info())
    print(druhe_auto.pujc_auto())
   
else:
    print("Zadej Škoda nebo Peugeot.")