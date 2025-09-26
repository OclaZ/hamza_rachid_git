import data
import users

user=data.utilisateurs
aime_livre=data.aime_livres
livres=data.livres

users.affichage_utilisateur_adultes(user)
users.affichage_noms_en_majuscule(user)
dic=users.dictionnaire_utilisateurs_livre(user,aime_livre)
print(dic)
users.affichage_dictionnaire(dic)




                          


