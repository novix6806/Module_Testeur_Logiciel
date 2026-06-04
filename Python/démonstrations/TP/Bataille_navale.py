# TP Mini Bataille-Navale
SEPARATEUR, FIN, LIMITE = '_', '=', 80
print("Mini Bataille Navale v0".center(LIMITE, SEPARATEUR))

INIT, MISS, HIT, DIMENSION = '?', '~', 'X', 4 # Constantes du jeu :

# Fonctions Lambda :
import random


separation = lambda nombre=LIMITE: print(SEPARATEUR * LIMITE)
pause = lambda: input((SEPARATEUR * (LIMITE // 2)) + "Appuyer sur 'Entrée' pour continuer…")

# Description des méthodes :
NAVIRE_CACHE = None


def initialiser_plateau():
    """Initialisation du plateau du jeu."""
    return [[INIT for _ in range(DIMENSION)] for _ in range(DIMENSION)]


def coordonnees_navire_a_cacher():
    """Retourne les coordonnées (colonne, ligne) aléatoires, afin de cacher un navire."""
    return random.randint(0, DIMENSION - 1), random.randint(0, DIMENSION - 1)


def afficher_plateau(un_plateau):
    """Affichage du plateau du jeu."""
    print("\n   ", end="")
    for colonne in range(DIMENSION):
        print(f"{colonne} ", end="")
    print()

    for ligne in range(DIMENSION):
        print(f"{ligne} | ", end="")
        for colonne in range(DIMENSION):
            print(f"{un_plateau[ligne][colonne]} ", end="")
        print()


def saisir_coordonnees():
    """Saisie des coordonnées par l'utilisateur d'un missile,
     sous la forme Colonne et Ligne avant de les retourner."""
    while True:
        try:
            la_colonne = int(input("Colonne (0 à 3) : "))
            la_ligne = int(input("Ligne (0 à 3) : "))
            if 0 <= la_colonne < DIMENSION and 0 <= la_ligne < DIMENSION:
                return la_colonne, la_ligne
            print("Coordonnées invalides. Veuillez entrer une valeur entre 0 et 3.")
        except ValueError:
            print("Veuillez entrer des nombres entiers.")


def lancer_missile(une_colonne, une_ligne):
    """Lancement d'un missile aux coordonnées indiquées en paramètre,
     puis retourn Vrai si touché ou Faux sinon."""
    global NAVIRE_CACHE
    return (une_colonne, une_ligne) == NAVIRE_CACHE


# Exécution du programme :
print("\nNouvelle partie :")
plateau = initialiser_plateau()
NAVIRE_CACHE = coordonnees_navire_a_cacher()
print("Trouvez le navire caché sur le plateau !")
separation()

while True:
    afficher_plateau(plateau)
    colonne, ligne = saisir_coordonnees()

    if plateau[ligne][colonne] in (MISS, HIT):
        print("Vous avez déjà tiré ici. Choisissez une autre case.")
        continue

    if lancer_missile(colonne, ligne):
        plateau[ligne][colonne] = HIT
        afficher_plateau(plateau)
        print("\nTouché ! Vous avez trouvé le navire.")
        break

    plateau[ligne][colonne] = MISS
    print("\nRaté !")

print((FIN * LIMITE) + "Fin de la partie !")