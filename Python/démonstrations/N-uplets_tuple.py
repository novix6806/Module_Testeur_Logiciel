# Démonstration: N-uplets (ou tuple) 

# Exemple de N-uplets (tuple):

ARC_EN_CIEL = 'rouge', 'orange', 'jaune', 'vert', 'bleu', 'indigo', 'violet'

JOURS = ('lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche',)

MOIS = ('janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre')

PLANETES = 'Soleil', "Mercure", "Vénus", "Terre", "Mars", "Jupiter", "Saturne", "Uranus", "Neptune"  # , "Pluton" 

SUITE_FIBONACCI = 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, '…'

SEPARATION, SYMB = 80, '_'

print(SEPARATION * SYMB)

print("Affichage des listes via la fonction 'print()'")

print("Couleurs de l'Arc-En-Ciel:", ARC_EN_CIEL)

print("Jour de la semaine:", JOURS)

print("Mois de l'année:", MOIS)

print("Les planètes du système solaire:", PLANETES)

print("La suite de Fibonacci:", SUITE_FIBONACCI)

print(SEPARATION * SYMB)

print("Affichage de quelques éléments issus des listes:")

print("L'arc-en-ciel va de la couleur", ARC_EN_CIEL[0], "à la couleur", ARC_EN_CIEL[-1])

print(SEPARATION * SYMB)

print("La semaine de travail, c'est du", JOURS[0], "au", JOURS[-3], ',')

print("mais il y a les 2 derniers jours de la semaine", JOURS[-2:], ".")

print("Il fait beau un jour sur deux", JOURS[::2], "!")

print("Il y a", len(MOIS), " mois dans l'année.")

print(SEPARATION * SYMB)

une_planete = input("\nSaisir le nom d'une planète ('Pluton' par défaut si vide): ").strip().capitalize() or "Pluton"

if PLANETES.count(une_planete) > 0:
    print(une_planete, "fait partie des planètes du système solaire, ")

    print("c'est la", str(PLANETES.index(une_planete)) + 'e', "planète à partir du soleil.")

else:
    print("<", une_planete.upper(), "> n'est pas considérée comme faisant partie des planètes du système solaire !")


def pause():
    input(SEPARATION // 2 * SYMB + "Appuyer sur 'Entrée' pour continuer…")


pause()


def afficher_liste(nom, liste, prefixe="\t-", separateur=",", fin='.'):
    """ Permet d'afficher les éléments d'une liste verticalement … [v0]"""

    # Les deux lignes suivantes peuvent être réécrites en une seule avec le walrus operator (à partir de Python 3.8)
    # if avec_numero := (type(prefixe) == type(0)) or prefixe.isnumeric():  # Indicateur pour la gestion de la numérotation
    avec_numero = (type(prefixe) == type(0))
    if avec_numero or prefixe.isnumeric():  # Indicateur pour la gestion de la numérotation
        zero = (int(prefixe) == 0)  # Gestion de l'indice ou d'un numéro 

    nb_items = len(liste)  # Nombre d'éléments 

    if len(nom):  # Affichage du nom de la liste, avec le nombre d'éléments 

        print(nom, '(' + str(nb_items) + ')', ':')

        # Parcours de la liste avec récupération des indices

        for i, item in enumerate(liste):

            if avec_numero:

                numero = i

                if not zero: numero += 1

                element = '\t' + str(numero) + '-'

            else:
                element = prefixe

            element += ' ' + str(item).capitalize()

            if len(separateur):  # Gestion du séparateur en fonction du dernier élément

                if (i + 1) < nb_items:
                    element += separateur

                else:
                    element += fin

            print(element)  # Afficher l'élément

        pause()

        print('')  # Passer une ligne vide

    print(SEPARATION * SYMB)

    print("Affichage des listes via la méthode 'afficher_liste()'")

afficher_liste("Couleurs de l'Arc-En-Ciel", ARC_EN_CIEL, "•")

afficher_liste("Jour de la semaine", JOURS, 123, '')

afficher_liste("Mois de l'année", MOIS, 12, '')

afficher_liste("Les planètes du système solaire", PLANETES, 0)

afficher_liste("La suite de Fibonacci", SUITE_FIBONACCI, "\t·", '')

print('_' * 64, "Fin de la démonstration")