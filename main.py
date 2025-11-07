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
van = False
for szam in adatok:
    if szam == 4:
        van = True
        break

if van:
    print("Van négyes")
else:
    print("Nincs négyes")
#4. Keressük meg, volt e 5ös
van5 = False
for i in range(len(adatok)):
    if adatok[i] == 5:
        van5 = True
        break

if van5:
    print(f" Van ötös, és a(z) {i}. elem.")
else:
    print("Nincs ötös.")


#5. Hány darab kilences volt?
db = 0
for szam in adatok:
    if szam == 9:
        db += 1

print(f" {db} darab kilences van")
#6. Mennyi a legnagyobb beírt szám
legnagyobb_szam = adatok[0]
for szam in adatok:
    if szam > legnagyobb_szam:
        legnagyobb_szam = szam

print(f"A legnagyobb szám {legnagyobb_szam}")
#7. Hanyadik indexen van a legkisebb elem?
minindex = 0

for i in range(1,len(adatok)):
    if adatok[i] < adatok[minindex]:
        minindex = adatok[i]

print(f"A legkisebb elem {adatok[minindex]} és a {minindex}. elem")
#8. Páros számok kiírása paros.txt-be
with open("paros.txt", "w", encoding="utf-8") as fout:
    for szam in adatok:
        if szam %2 == 0:
            print(szam, file=fout)


