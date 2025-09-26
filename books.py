import data

Livres = data.livres
Livres.sort(key=lambda x: x["année"], reverse=True)
print(Livres)

def Récent_Ancien(MyList):
    ancien = Livres[-1]
    print(ancien)
    Récent = Livres[0]
    print(Récent)

def dectionaire(MyList):

Récent_Ancien(Livres)