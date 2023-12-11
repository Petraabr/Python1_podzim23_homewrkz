
def zkontroluj_cislo(telefonni_cislo):
    delka_cisla = len(telefonni_cislo)
    #Složené podmínky, pokud je délka čísla 9 nebo (or) (pokud je délka čísla 13 a zároveň (and) první 4 znaky čísla rovny +420)
    #Pokud jedna z podmínek platí vrací True(číslo je v pořádku) jinak False
    if delka_cisla == 9 or (delka_cisla == 13 and telefonni_cislo[:4] == "+420"):
        return True
    else: 
        return False
        
def vypocitej_cenu_sms(sms):
    delka_sms = len(sms)
   
    cena_sms = int(delka_sms/180)*3


  
    if (delka_sms%180 > 0):
        cena_sms += 3

    print(f"Cena sms je: {cena_sms}.")



telefonni_cislo = input("Zadej telefonní číslo: ")
print (telefonni_cislo)

if zkontroluj_cislo(telefonni_cislo):
    
    vloz_text = input("Prosím napiš text sms: ")
    print(vloz_text)
   
    vypocitej_cenu_sms(vloz_text)
else:
    print("Prosím použij telefonní číslo ve správném formátu!") 