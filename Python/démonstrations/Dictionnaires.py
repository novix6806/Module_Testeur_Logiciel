# Démonstration : Les dictionnaires (dict)
SYMB, NB = '_', 56
def pause(): input('\n' + (SYMB * NB) + "Appuyer sur 'Entrée' pour continuer…\n")

print("Création de dictionnaires (vide) :")
ma_recette = dict()
print("ma_recette = dict()\n\t", ma_recette, type(ma_recette))
mes_ingredients = {}
print("mes_ingredients = {}\n\t", mes_ingredients, type(mes_ingredients))
pause()

print("Création d'un autre ensemble des_ustensiles :")
pokemon = "Pikachu" # Pokemon Go !
des_ustensiles = {"Recipient": "Saladier", "Feuille Sulfurisée": 1, "Plaque": 1,
              "Cuillère à soupe": 2, "Spatule": 1, pokemon: 1, "Four": 1, "Couteau Électrique": 1}
print("des_ustensiles =", des_ustensiles, type(des_ustensiles))
print("\nN.B. : Un intrus s'est glissé dans le dictionnaire des_ustensiles... Il s'agit d'un Pokémon ({}).".format(pokemon))
pause()

print("Nous allons supprimer l'élément intru de cet ensemble comme ci-dessous:")
print("des_ustensiles.pop('{0}') ou del des_ustensiles['{0}']".format(pokemon))
des_ustensiles.pop(pokemon)  # del des_ustensiles[pokemon]
print("\ndes_ustensiles (sans Pokémon) =", des_ustensiles)
pause()

print("Création d'un dictionnaire renseigné pour les étapes à suivre, soit la_procedure (N°/Opération) :")
la_procedure = {1: "Mélanger tous les ingrédients dans le Saladier",
             6: "Sortir les gâteaux du Four",
             3: "Sur une feuille sulfurisée (ou silicone), étaler la pâte en 2 ou 3 boudins larges",
             5: "Attendre 15 à 20 minutes de cuisson",
             7: "Découper en tronçons de 2cm (avec le Couteau Électrique)",
             4: "Placer la plaque dans le four, faire cuire à 180°c la préparation",
             2: "Laisser reposer la préparation un peu",
             8: "Se mange froid (c'est meilleur)",
             }
print("la_procedure = \n", la_procedure, type(la_procedure))
print("\nN.B. : Observez que depuis la version de Python 3.7, le dictionnaire conserve l'ordre d'insertion, car les étapes ont été mélangées.")
pause()

print("Nous allons ordonnancer les étapes de la_procedure, à partir de la méthode sorted().")
print("sorted() ne modifie pas l'objet passé en paramètre, mais retourne une nouvelle liste contenant des N-Uplets (Clef, Valeur).")
print("\nla_procedure = sorted(procedure.items())")
la_procedure = sorted(la_procedure.items()) # sorted(iterable) retourne une nouvelle list contenant des tuples (Clef, Valeur)
print("\nla_procedure (trié /list+tuples) = \n", la_procedure, type(la_procedure))
pause()

print("Conversion d'une Liste(N-Uplets) en dictionnaire :\n la_procedure = dict(la_procedure)")
la_procedure = dict(la_procedure) # Conversion en dictionnaire dict(Clef:Valeur)
print("\nla_procedure (trié /dict) = \n", la_procedure, type(la_procedure))
pause()

print("Ajout des éléments dans mes_ingredients :")
mes_ingredients["Œuf"] = 2  # 2 Oeufs entiers (en omelette)
mes_ingredients["Sucre"] = "180g"
mes_ingredients["Sachet Sucre Vanillé"] = 2
mes_ingredients["Beurre Fondu"] = "125g"
mes_ingredients["Amande"] = "125g"  # 125g d'amandes non émondées (avec la peau)
mes_ingredients["Farine"] = "300g"
mes_ingredients["Zeste"] = 1  # zeste orange ou citron (facultatif)
print("mes_ingredients = ", mes_ingredients)
pause()

print("Ajout d'informations dans ma_recette, et association dans ma_recette des autres ensembles (mes_ingredients, des_ustensiles, la_procedure) :")
ma_recette["Titre"] = "Croquants aux Amandes"
ma_recette["Temps"] = "< 30 min."
ma_recette["Difficulté"] = "très facile"
ma_recette["Note"] = "~4.5/5"
ma_recette["Ingrédients"] = mes_ingredients
ma_recette["Ustensiles"] = des_ustensiles
ma_recette["Procédure"] = la_procedure
print("ma_recette =\n", ma_recette, type(ma_recette))
pause()
print(NB * SYMB, '\n')

def parcourir_dictionnaire(un_ensemble, pattern="• {clef} : {valeur}", niveau=1):
    """Fonction permettant de parcourir un dictionnaire avec affichage des clés/valeurs, 
        ainsi que de parcourir s'il contient lui-même des dictionnaires par récursivité."""
    indentation = '\t' * niveau  # Gestion de l'indentation en fonction du niveau (/recursivité)
    for clef, valeur in un_ensemble.items():
        if type(valeur) in [dict]:  # Est-ce que la valeur est un dictionnaire
            print(indentation, "- {} :".format(clef))
            # Fonction récursive (s'appelle elle-même)
            parcourir_dictionnaire(valeur, niveau=niveau + 1)
        else:
            print(indentation, pattern.format(clef=clef, valeur=valeur))

print("L'auteur de la recette \"{}\", que nous allons vous présenter, est '{}', et il a obtenu la note de {} !".format(
    ma_recette['Titre'],
    ma_recette.get("Auteur", "Inconnu"),
    ma_recette['Note']))
print("Vous trouverez ci-dessous la fiche de la recette.\nBonne préparation et bonne dégustation.\n")
print("La recette du jour".title().center(NB, SYMB) + (SYMB * NB))
parcourir_dictionnaire(ma_recette)

print('_' * 64, "Fin de la démonstration")