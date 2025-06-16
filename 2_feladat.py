#2. Feladat
#arato-cseplo gep megtett utjanak hossza

def aratasi_ut(hosszusag, szelesseg, vagoasztal):
    sorok_szama = szelesseg // vagoasztal
    sor_hossz = hosszusag - vagoasztal
    megtett_ut = (sorok_szama * sor_hossz) + ((sorok_szama - 1) * vagoasztal)

    return megtett_ut

print("2.feladat: Arato-cseplogep megtett utjanak hossza:")
hosszusag = int(input("\tAdja meg a terulet hosszusagat meterben: "))
szelesseg = int(input("\tAdja meg a terulet szelesseget meterben: "))
vagoasztal = 0
while vagoasztal < 3 or vagoasztal >12:
    vagoasztal = int(input("\tAdja meg az arato-cseplo szelesseget meterben (3-12): "))

print(f"\n\tAz Arato-cseplogep altal megtett teljes ut: {aratasi_ut(hosszusag, szelesseg, vagoasztal)} meter")
maradek_terulet = (szelesseg % vagoasztal) * hosszusag
print(f"\tA maradek terulet: {maradek_terulet} m2")