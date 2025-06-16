#1. Feladat
#Elektromos auto hatotav kalkulator

print("1.Feladat: Hatotav kalkulator")
toltottseg = int(input("\tAdja meg az akkumlator toltottsegi allapotat(%): "))

if 1 > toltottseg or 100 < toltottseg:
    print("Nem megfelelo adat!")
elif toltottseg < 20:
    print("Kerem minimum 20%-os akkumulatorral induljon utnak!")
else:
    megteheto = (toltottseg-5) *5
    print(f"\tAz auto {megteheto} kilomtert tehet meg!")
