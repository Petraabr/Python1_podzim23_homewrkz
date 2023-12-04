jmeno = "Petra"
print(jmeno + "@czechitas.cz" )

#Napiš program, který bude obsahovat proměnnou jmeno_a_prijmeni. Obsah proměnné načti od uživatele pomocí funkce input. Tvůj program postupně vypíše několik způsobů formátování jména:
jmeno_a_prijmeni =  input("Zadej své jméno a příjmení, prosím: ")
print(jmeno_a_prijmeni)

#všechna písmena velká (vypíše např. JANA MALÁ)
print((jmeno_a_prijmeni).upper())
#všechna písmena malá (vypíše např. jana malá)
print((jmeno_a_prijmeni.lower()))
#standardní varianta - první písmeno velké, další malá (vypíše např. Jana Malá)
jmeno_a_prijmeni = str(jmeno_a_prijmeni)
print(jmeno_a_prijmeni)
#iniciály (vypíše např. J. M.)
#křestní jméno zkrácené na první písmeno a příjmení, pokud je křestní jméno delší než 5 znaků. Jinak vypíše standardní variantu, tj. první písmeno velké, další malá (u vstupu Jarmila Malá by došlo ke zkrácení křestního jména, zatímco u vstupu Jana Malá nikoliv)
#Zaexperimentuj s různými vstupy od uživatele (co třeba JaNA maLá? 