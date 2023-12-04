sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}



zadej_kod_vyrobku = input("Zadejte kod výrobku: ")
zadej_pozadovany_pocet_kusu = int(input("Zadejte požadovaný počet kusů výrobku: "))

if zadej_kod_vyrobku in sklad:
        
    if sklad.get(zadej_kod_vyrobku) <= zadej_pozadovany_pocet_kusu:
          print(f"Na skladě je omezené množství kusů výrobku.")
          sklad.pop(zadej_kod_vyrobku)
    else: 
        print(f"Výrobek {zadej_kod_vyrobku} je skladem.")
else: print (f"Výrobek nemáme skladem.")

sklad[zadej_kod_vyrobku] = sklad[zadej_kod_vyrobku] - zadej_pozadovany_pocet_kusu