#kineski horoskop 
"""Prema staroj legendi, Buda je pozvao sve životinje na veliku proslavu.Međutim, 
samo 12 životinja se odazvalo pozivu: pacov,bivo, tigar, zec, zmaj, zmija, konj, 
koza, majmun, pjetao, pas i svinja. Zbog ukazanog poštovanja Buda je odlučio da 
svaka životinja dobije jednu godinu u kojoj će posebno biti poštovana.
U kineskom horoskopu svakih 12 godina ciklus se ponavlja a svaki čovjek pripada 
znaku koji je vladao u godini u kojoj je rodjen. Vaš zadatak je da na osnovu 
godine rođenja osobe, odredite njen astrološki znak i ispišete korisniku na  ekrenu.
- broj ciklusa je jednak ostatku djeljenja sa 12 prethodno oduzete godine rodjenja od 1900
- uslov je da korisnik mora da unese godinu vecu od 1900
- korisniku treba upozoriti ukoliko unese manje od cetri cifre """

astroloske_zivotinje =['pacov', 'vo', 'tigar', 'zec', 'zmaj', 'zmija',
'konj','koza', 'majmun', 'pjetao', 'pas', 'svinja']

godina_rodjenja=int(input("Unesite godinu rodjenja"))
def odredi_horoskop(godina_rodjenja):
    if godina_rodjenja>1900:
        razlika_godina=godina_rodjenja-1900
        broj_ciklusa=razlika_godina%12
        return astroloske_zivotinje.pop(broj_ciklusa)
    if len(str(godina_rodjenja))<4:
        poruka ="Greška"
        return poruka
print(odredi_horoskop(godina_rodjenja))
