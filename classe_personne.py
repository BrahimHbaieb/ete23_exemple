class Personne:
    def __init__(self, p_nom, p_prenom, p_age):
        self.nom = p_nom
        self.prenom = p_prenom
        self.age = p_age

    def afficher(self):
        print('Je suis ', self.prenom, 'et j ai', self.age)

# Création des objets

liste = []
liste.append(Personne('babari', 'raouf', 31))
liste.append(Personne('bachir', 'Fikry', 25))
liste.append(Personne('Nabil', 'Agsous', 40))

# Les objets de la même classe se comportemt souvent de la même manière ...
for x in liste:
    x.afficher()