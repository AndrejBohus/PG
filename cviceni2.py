# def main():
# if __name__ == "__main__":
#     main()
# def cviceni_2():
#     # seznam
#     seznam = [1,2,3,4,5]
#     # vzit treti prvek a krat 2
#     seznam[2]*=2
#     # pridani seznamu o cislo 55
#     seznam.append([55])
#     # Sort funkce
#     seznam.sort()
#     # Reverse funkce
#     seznam.reverse()
#     # print
#     print(seznam)
# if __name__ == "__main__":
#     cviceni_2()

# def vracet_3_prvek_ze_seznamu(seznam):
#     if len (seznam) >= 3:
#         return seznam [2]
#     else:
#         return None
# if __name__ == "__main__":
#     x = [1,2]
#     print(vracet_3_prvek_ze_seznamu([x]))
#     y = [1,2,3,4,5,6]
#     print(vracet_3_prvek_ze_seznamu([y]))

# def median_seznamu(cisla):
#     return sum(cisla)/len(cisla)
# if __name__ == "__main__":
#     cisla = [1,2,3,4,5]
#     print(median_seznamu(cisla))

student = {
    "Jmeno" : "Jan",
    "Prijmeni" : "Novak",
    "vek" : 22,
    "znamky" : [1,2,3,1,2,1]
}
# print(student["Prijmeni"])
# print(student["znamky"][2])
student["vek"] = 21
student["obor"] = "AEFP"
print(student)

def naformatuj_text(zak):
    jmeno = zak["Jmeno"]
    prijmeni = zak["Prijmeni"]
    vek = zak["vek"]
    obor = zak["obor"]
    
    text = f"Student: {}"
if __name__ == "__main__":
    student = {
    "Jmeno" : "Jan",
    "Prijmeni" : "Novak",
    "vek" : 22,
    "znamky" : [1,2,3,1,2,1]
    }
    # print(student["Prijmeni"])
    # print(student["znamky"][2])
    # student["vek"] += 1
    # student["obor"] = "AEFP"
    print(naformatuj_text(student))