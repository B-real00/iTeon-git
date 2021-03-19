#  ZADATAK 1
'''
Prema staroj legendi, Buda je pozvao sve životinje na veliku proslavu.Međutim, 
samo 12 životinja se odazvalo pozivu: pacov,bivo, tigar, zec, zmaj, zmija, konj, O
koza, majmun, pjetao, pas i svinja. Zbog ukazanog poštovanja Buda je odlučio da 
svaka životinja dobije jednu godinu u kojoj će posebno biti poštovana.
U kineskom horoskopu svakih 12 godina ciklus se ponavlja a svaki čovjek pripada 
znaku koji je vladao u godini u kojoj je rodjen. Vaš zadatak je da na osnovu 
godine rođenja osobe, odredite njen astrološki znak i ispišete korisniku na  ekrenu.
- broj ciklusa je jednak ostatku djeljenja sa 12 prethodno oduzete godine rodjenja od 1900
- uslov je da korisnik mora da unese godinu vecu od 1900
- korisniku treba upozoriti ukoliko unese manje od cetri cifre '''

astroloske_zivotinje =['pacov', 'vo', 'tigar', 'zec', 'zmaj', 'zmija',
'konj','koza', 'majmun', 'pjetao', 'pas', 'svinja']

def kineski_horoskop():
    godine_korisnika=int(input("Unesite godinu Vaseg rodjenja: "))
    if godine_korisnika>1900:
        broj_ciklusa=(godine_korisnika-1900)%12
        astroloski_znak=astroloske_zivotinje[broj_ciklusa]
        return astroloski_znak
    else:
        return "Pogresan unos, pokusajte ponovo!"
        

print("Vas astroloski znak je :", kineski_horoskop())



