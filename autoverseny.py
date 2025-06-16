#3.feladat: Autoverseny osztaly letrehozasa

class Autoverseny:
    #Név;Születési év;Ország;Autómárka;Versenyidő
    def __init__(self,sor:str):
        adatok = sor.strip().split(";")
        self.nev = adatok[0]
        self.ev = int(adatok[1])
        self.orszag = adatok[2]
        self.marka = adatok[3]
        self.ido = float(adatok[4])