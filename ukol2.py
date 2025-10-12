def cislo_text(cislo):
    # funkce zkonvertuje cislo do jeho textove reprezentace
    # napr: "25" -> "dvacet pět", omezte se na cisla od 0 do 100
    # text_cisel = ["nula", "jedna", "dva"]
    # return text_cisel[cislo]
    jednotky = ["", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět"]
    deset_az_devatenact = ["deset", "jedenáct", "dvanáct", "třináct", "čtrnáct", "patnáct", "šestnáct", "sedmnáct", "osmnáct", "devatenáct"]
    desitky = ["", "", "dvacet", "třicet", "čtyřicet", "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"]
    
    if cislo == 0:
        return "nula"
    if cislo == 100:
        return "sto"
    
    des = cislo // 10  
    jed = cislo % 10  

    if des == 1:
        return deset_az_devatenact[jed]
    
    if des >= 2:
        if jed == 0:
            return desitky[des]
        else:
            return desitky[des] + " " + jednotky[jed]
    
    return jednotky[jed]
    # řešení pomocí podmínek otestovat jednotlivé části čísla (desítky, jednotky)
    # druhej seznam po 10 (10,20,30,40,50,60 atd..)
    # k tomu prilepovat z dalsiho seznamu (1,2,3,4,5,6,7,8,9)
if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(int(cislo))
    print(text)
