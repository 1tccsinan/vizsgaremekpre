#1. Adatok beolvasása listába
adatok = []
with open("data.txt", "r",encoding="utf-" ) as fin:
    for sor in fin:
        adatok.append(int(sor))

print(adatok)

#2. Adatok átlaga
atlag = sum(adatok)/len(adatok)
print(f"A beolvasott elemek átlaga: {atlag:.2f}")

#3. Döntsük el, hogy volt-e 4es
#4. Keressük meg, volt e 5ös
#5. Hány darab kilences volt?
#6. Mennyi a legnagyonn beírt szám
#7. Hanyadik indexen van a legkisebb elem?
#8. Páros számok kiírása paros.txt-be
