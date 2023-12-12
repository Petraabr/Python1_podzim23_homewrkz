import pandas

tabulka = pandas.read_csv('adopce-zvirat.csv', sep=";")
tabulka.info()
print(tabulka.info())
tabulka.head()
print(tabulka.head())

print(f"Počet řádků v tabulce: {tabulka.shape[0]}")
print(f"Počet sloupců v tabulce: {tabulka.shape[1]}")
print(f"Názvy sloupců v tabulce: {tabulka.columns}")

nazev = tabulka[["nazev_cz", "nazev_en"]]
print(nazev.iloc[[34]])



