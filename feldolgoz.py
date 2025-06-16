#3.2 feladat: autoverseny.txt feldolgozasa
from autoverseny import Autoverseny
from pathlib import *

def beolvas(fajl: Path) -> list[Autoverseny]:
    versenyek = []
    with open(fajl, "r", encoding="utf-8") as file:
        next(file)
        for sor in file:
            versenyek.append(Autoverseny(sor))
    return versenyek

def versenyzok_szama(lista: list[Autoverseny]) -> int:
    return len(lista)

def adott_evben_szuletett_versenyzo(lista:list[Autoverseny], adott_ev : int):
    versenyzok = []
    for v in lista:
        if v.ev == adott_ev:
            versenyzok.append(v.nev)
    if not versenyzok:
        return "Nincs ilyen versenyzo"
    return versenyzok

def verseny_nyertese(lista:list[Autoverseny]):
    gyoztes = lista[0]
    for v in lista:
        if v.ido < gyoztes.ido:
            gyoztes = v
    return gyoztes

def orszagok_szerint(lista: list[Autoverseny]) -> dict[str,int]:
    stat: dict[str, int] = {}
    for v in lista:
        if v.orszag in stat.keys():
            stat[v.orszag] += 1  # Ha már szerepel az ország, növeljük a számlálót
        else:
            stat[v.orszag] = 1 # Ha még nem szerepel, 1-gyel indítjuk
    for o, v in stat.items():
        if v > 2:
            print(f"\t{o}: {v} versenyzo")
