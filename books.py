import data

aimeLivers = data.aime_livres
Livres = data.livres
Livres.sort(key=lambda x: x["année"], reverse=True)
print(Livres)

def Récent_Ancien(MyList):
    ancien = Livres[-1]
    print(ancien)
    Récent = Livres[0]
    print(Récent)

def dectionaire(MyList):
    list = []
    dict = []

    for aimeLiver in MyList:
        list.append(aimeLiver[1])
    print(list)

    for i in list:
        Count = list.count(i)
        if { "id": i, "count": Count } not in dict:
            dict.append({ "id": i, "count": Count })

    print(dict)


Récent_Ancien(Livres)
dectionaire(aimeLivers)