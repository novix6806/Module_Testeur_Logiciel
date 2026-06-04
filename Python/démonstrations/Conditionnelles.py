# Démonstration : Les conditionnelles
age = int(input("Quel est votre âge ? ")) # Conversion du texte en nb. entier
AGE_MAJORITE = 18 # Limite entre une personne majeure/mineure
# Étape n°1 : Vérification Si Majeur / âge
majeur = False # Valeur par défaut
if age >= AGE_MAJORITE:
    majeur = True
print("E1) Vous êtes majeur :", majeur)
# Étape n°2 : Vérification Si Majeur ou Mineur
if age >= AGE_MAJORITE:
    majeur_ou_mineur = "majeur"
else:
    majeur_ou_mineur = "mineur"
print("E2) Vous êtes", majeur_ou_mineur, "!")
# Étape n°3 : Vérification Si Senior, ou Majeur, ou Mineur
AGE_SENIOR = 70 # Âge d'un jeune sénior
if age >= AGE_SENIOR:
    categorie_age = "senior"
elif age >= AGE_MAJORITE:
    categorie_age = "majeur"
else:
    categorie_age = "mineur"
print("E3) Vous êtes donc un", categorie_age, "!")
print('_' * 64, "Fin de la démonstration") # Répétion du caractère UNDERSCORE 64 fois

# Étape n°4 : Qualification en fonction de l'âge
TRENTE = 30 # Âge d'un trentenaire
QUARANTE = 40 # Âge d'un quarantenaire
CINQUANTE = 50 # Âge d'un cinquantenaire
SOIXANTE = 60 # Âge d'un soixantenaire
# Python autorise la combinaison des opérateurs de comparaison
if 0 < age < AGE_MAJORITE:
    categorie_age = "mineur"
elif AGE_MAJORITE <= age < TRENTE:
    categorie_age = "jeune adulte"
elif TRENTE <= age < QUARANTE:
    categorie_age = "trentenaire"
elif QUARANTE <= age < CINQUANTE:
    categorie_age = "quarantenaire"
elif CINQUANTE <= age < SOIXANTE:
    categorie_age = "cinquantenaire"
elif SOIXANTE <= age < AGE_SENIOR:
    categorie_age = "soixantenaire"
elif AGE_SENIOR <= age:
    categorie_age = "senior"
else: # par défaut
    categorie_age = "indéterminé"
print("E4) Catégorie/Âge =", categorie_age)
# Répétion du caractère UNDERSCORE 64 fois
print('_' * 64, "Fin de la démonstration") # Fin de l'algorithme