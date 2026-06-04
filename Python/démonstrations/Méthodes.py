# Démonstration : Création et utilisation de méthodes v0
# Algorithme non modulaire (ou monolithique)

# NB_CAR, SYMB = 80, '#'

# print(NB_CAR * SYMB)
# print("Bienvenue dans cette démonstration sur les fonctions et paramètres".center(NB_CAR))
# print(NB_CAR * SYMB)
# choix = int(input("""Demande de saisie d'un entier à l'utilisateur :
# \t1 - Afficher une catégorie d'âge
# \t2 - Afficher une table de multiplication
# \t3 - Afficher les couleurs de l'arc en ciel
# Quel est votre choix ?\n""") or 0)
# print(NB_CAR * SYMB)
# print("")  # Ligne de Séparation

# TAB, RAL = '\t', '\n'  # Tabulation, Retour À la Ligne
# if choix == 1:  # Choix n°1
#     print("Catégorie en fonction de l'âge".center(NB_CAR))
#     print(NB_CAR * SYMB)
#     # Conversion du texte en nombre
#     age = float(input("Quel est votre âge ? "))
#     # Limite entre une personne majeure/mineure et senior
#     AGE_MAJORITE, AGE_SENIOR = 18, 70
#     # Âge d'un (N x dix)tenaire
#     TRENTE, QUARANTE, CINQUANTE, SOIXANTE = 30, 40, 50, 60
#     if 0 < age < AGE_MAJORITE:
#         categorie_age = "mineur"
#     elif AGE_MAJORITE <= age < TRENTE:
#         categorie_age = "jeune adulte"
#     elif TRENTE <= age < QUARANTE:
#         categorie_age = "trentenaire"
#     elif QUARANTE <= age < CINQUANTE:
#         categorie_age = "quarantenaire"
#     elif CINQUANTE <= age < SOIXANTE:
#         categorie_age = "cinquantenaire"
#     elif SOIXANTE <= age < AGE_SENIOR:
#         categorie_age = "soixantenaire"
#     elif AGE_SENIOR <= age:
#         categorie_age = "senior"
#     else:  # par défaut
#         categorie_age = "indéterminé"
#     print("Catégorie/Âge =", categorie_age)
# elif choix == 2:  # Choix n°2
#     print("Table de Multiplication".center(NB_CAR))
#     print(NB_CAR * SYMB)
#     nb = int(input("Indiquer un nombre ? "))
#     for i in range(10):
#         m = i + 1
#         print(m, "x", nb, "=", m * nb)
#     # Fin du bloc itératif
# elif choix == 3:  # Choix n°3
#     print("Voici les couleurs de l'arc-en-ciel :")
#     print(NB_CAR * SYMB)
#     ARC_EN_CIEL = "rouge, orange, jaune, vert, bleu, indigo, violet"
#     print(TAB + ARC_EN_CIEL.replace(', ', RAL + TAB).title())
# else:  # Choix n°?

#     print("Désolé, mais ce choix n'est pas dans la liste des propositions !")

# print('_' * 64, "Fin de la démonstration")


#version refactorisée avec des fonctions et paramètres
# Démonstration : Création et utilisation de méthodes v1
# Algorithme modulaire

# Description des méthodes + docstring :

TAB, RAL = '\t', '\n' # Tabulation, Retour À la Ligne

def afficher_info(message, nb_car=80, symb='#'):
    """Permet d'afficher un message, 
    avec une séparation de 80 caractères (par défaut) avant et après le message,
    répété à partir du symbôle # (par défaut). 
    Puis affiche un ligne vide."""
    print(RAL + symb * nb_car) # Ligne de Séparation

    print(message.center(nb_car))
    print(symb * nb_car) # Ligne de Séparation

def saisir_nombre(question, details=""):
    """Invite l'utilisateur à saisir au clavier un numérique, 
    avant de retourner un nombre entier (par défaut 0 si rien de saisie)).
    Des détails précisant la question peuvent être affiché avant en fonction (par défaut vide)."""
    if len(details) > 0:
        print(details)
    return int(float(input(question + RAL) or 0)) # Conversion du texte en décimal, puis en entier (0 par défaut)

def donner_categorie_age(age):
    """Retourne une catégorie en fonction d'un âge"""
    AGE_MAJORITE, AGE_SENIOR = 18, 70 # Limite entre une personne mineure/majeure/senior

    TRENTE, QUARANTE, CINQUANTE, SOIXANTE = 30, 40, 50, 60 # Âge d'un (N x dix)tenaire

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
    return categorie_age # Retourne la catégorie

def afficher_table_multiplication(nb, limite=10):
    """Affiche une table de multiplication en fonction d'un nombre,
    et d'une limite (10 par défaut))"""
    print("Table de multiplication de", nb, "jusqu'à", limite, ":")
    for i in range(limite):
        m = i + 1
        print(TAB, m, "x", nb, "=", m * nb)
    # Fin du bloc itératif

def afficher_couleurs_ArcEnCiel():
    afficher_info("Voici les couleurs de l'arc-en-ciel")
    ARC_EN_CIEL = "rouge, orange, jaune, vert, bleu, indigo, violet"
    print(TAB + ARC_EN_CIEL.replace(', ',RAL + TAB).title())

def main(): # Programme Principal


    afficher_info("Bienvenue dans cette démonstration sur les fonctions et paramètres")

    choix = saisir_nombre("Quel est votre choix ?",
        """Demande de saisie d'un entier à l'utilisateur :
        1 - Afficher une catégorie d'âge
        2 - Afficher une table de multiplication
        3 - Afficher les couleurs de l'arc en ciel""")

    if choix == 1: #Choix n°1

        afficher_info("Catégorie en fonction de l'âge")
        age = saisir_nombre("Quel est votre âge ? ")
        categorie = donner_categorie_age(age)
        print("Catégorie/Âge =", categorie)
    elif choix == 2: #Choix n°2

        afficher_info("Table de Multiplication")
        nombre = saisir_nombre("Indiquer un nombre ? ")
        afficher_table_multiplication(nombre)
    elif choix == 3: #Choix n°3

        afficher_couleurs_ArcEnCiel()
    else: #Choix n°?

        afficher_info("Désolé, mais ce choix n'est pas dans la liste des propositions !")

main() # Appel du programme principal

print('_' * 64, "Fin de la démonstration")