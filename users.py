from data import utilisateurs

def filter_utilisateur_adulte(users):
    return [user for user in users if user[3] >= 18]

adults = filter_utilisateur_adulte(utilisateurs)
print(adults)