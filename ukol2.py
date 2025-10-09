def cislo_text(cislo):
    # funkce zkonvertuje cislo do jeho textove reprezentace
    # napr: "25" -> "dvacet pět", omezte se na cisla od 0 do 100
    text_cisel = ["nula", "jedna", "dva"]
    return text_cisel[cislo]
    # řešení pomocí podmínek otestovat jednotlivé části čísla (desítky, jednotky)
    # druhej seznam po 10 (10,20,30,40,50,60 atd..)
    # k tomu prilepovat z dalsiho seznamu (1,2,3,4,5,6,7,8,9)
if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(int(cislo))
    print(text)
