from feldolgoz import *
from pathlib import *

helyimappa = Path(__file__).parent.resolve()
autoversenyek = helyimappa/ "autoversenyek.txt"

fajl = beolvas(autoversenyek)

print("3.2 feladat: A fajl beolvasva!")

print(f"3.3 feladat: A versenyen {versenyzok_szama(fajl)} versenyzo indult.")
evszam = int(input("3.4 feladat: Kerek egy szuletesi evet: "))
print(f"Versenyzok: {adott_evben_szuletett_versenyzo(fajl, evszam)}")
gyoztes = verseny_nyertese(fajl)
print(f"3.5. feladat: A verseny gyoztese:")
print(f"\tNev: {gyoztes.nev}")
print(f"\tSzuletesi ev: {gyoztes.ev}")
print(f"\tOrszag:{gyoztes.orszag}")
print(f"\tAutomarka:{gyoztes.marka}")
print(f"\tVersenyido:{gyoztes.ido}")
print(f"3.6. feladat: Versenyzok orszaga stat:")
orszagok_szerint(fajl)