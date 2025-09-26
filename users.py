from data import utilisateurs
from data import aime_livres

def filter_utilisateur_adultes(users):
        if users[3] >= 18:
            return True

def noms_en_majuscule(users):
    return users[1].upper() , users[2].upper()

def dictionnaire_utilisateurs_livre(lst_user,lst_aime_livrea):
    dictio={}
    for (id_user, prenom, nom, age) in lst_user:
    
        livres_aimes = [titre for (id_livre, titre) in lst_aime_livrea if id_livre == id_user]
        dictio[id_user] = {
            "nom_complet": f"{prenom.upper()} {nom.upper()}",
            "age": age,
            "livres": livres_aimes
    }
    return dictio
   
def affichage_dictionnaire(dictio):
    for info in dictio.values():
        livres_names = "', '".join(info["livres"])
        print(f"{info['nom_complet']} ({info['age']} ans) aime : '{livres_names}'")


# adultes = list(filter(filter_utilisateur_adultes, utilisateurs))
# print(adultes)
# noms_maj=list(map(noms_en_majuscule, utilisateurs))
# print(noms_maj)
dictionnaire=dictionnaire_utilisateurs_livre(utilisateurs,aime_livres)
print(dictionnaire)
affichage_dictionnaire(dictionnaire)