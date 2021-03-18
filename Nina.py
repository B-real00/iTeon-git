astroloske_zivotinje =['pacov', 'vo', 'tigar', 'zec', 'zmaj', 'zmija',
'konj','koza', 'majmun', 'pjetao', 'pas', 'svinja']
def horoskop():
    godina_rodjenja=int(input("Unesite godinu rodjenja:"))
    if godina_rodjenja>1900:
        ciklus=(godina_rodjenja-1900)%12
        znak=astroloske_zivotinje[ciklus]
        return znak
        
    else:
        return "Pogresan unos. Godina rodjenja mora biti veca od 1900. Pokusajte ponovo!"
    

print(horoskop())