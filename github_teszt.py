szamok = []

for i in range(5):
    szam = int(input("Kérek egy számot: "))
    szamok.append(szam)

atlag=0.0

for szam in szamok:
    atlag += szam
    
atlag = atlag / len(szamok)

print(f"a számok átlaga {atlag}")