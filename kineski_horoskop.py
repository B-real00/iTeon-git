#  ZADATAK 1
'''
Prema staroj legendi, Buda je pozvao sve životinje na veliku proslavu.Međutim, 
samo 12 životinja se odazvalo pozivu: pacov,bivo, tigar, zec, zmaj, zmija, konj, 
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

godina=int(input('Unesi godinu rodjenja: '))   
broj_ciklusa=(godina-1900)%12
for i in range(12):
    if broj_ciklusa==i:
        print('Vas astroloski znak u kineskom horoskopu je: ', astroloske_zivotinje[i])


def is_valid(godina):
    if int(godina) > 1900 and len(godina) >= 4:
        return True
    else:
        return False
def ciklus(godina):
    res = int(godina) - 1900
    return res%12

godina = input("Unesite godinu: ")
while is_valid(godina) == False:
    godina = input("Unesite godinu: ")
print(astroloske_zivotinje[ciklus(godina)])