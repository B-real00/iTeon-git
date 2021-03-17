#kineski horoskop

astroloske_zivotinje =['pacov', 'vo', 'tigar', 'zec', 'zmaj', 'zmija',
'konj','koza', 'majmun', 'pjetao', 'pas', 'svinja']

godinaRodjenja = int(input("Unesite godinu rodjenja:"))
def astroloskiZnak(godinaRodjenja):
    if godinaRodjenja > 1900 and godinaRodjenja < 2022:
        brojCiklusa = (godinaRodjenja - 1900) % 12
        poruka = astroloske_zivotinje[brojCiklusa]
        return poruka

    else:
        poruka = "Greška"
        return poruka
       
odgovor = astroloskiZnak(godinaRodjenja)
print(odgovor)