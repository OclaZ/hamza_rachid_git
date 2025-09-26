import data

aimeLivers = data.aime_livres
Livres = data.livres
Users = data.utilisateurs
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

def dexupardeux(MyList):
    i =0;
    while i < len(MyList):
        print(f"Page {(i//2)+1} :")
        print(MyList[i])
        if i+1 < len(MyList):
            print(MyList[i+1])
        i+=2

Récent_Ancien(Livres)
dectionaire(aimeLivers)
dexupardeux(Users)