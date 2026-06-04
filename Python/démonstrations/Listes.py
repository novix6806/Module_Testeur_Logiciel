# Démonstration : Les listes (list)

def pause(): input('\n' + ('_' * 48) + "Appuyer sur 'Entrée' pour continuer…\n")

# Composition du Système Solaire :
soleil = "Soleil"
liste_planetes_telluriques = ("Mercure", "Vénus", "Terre", "Mars", )  # N-Uplets (tuple)
liste_planetes_joviennes = ("Jupiter", "Saturne", "Uranus", "Neptune", )  # ou géante gazeuse
liste_planetes_naines = ["Ceres", "Pluton", "Charon", "Hauméa", "Makémaké", "Éris", ]  # Liste modifiable

# Création d'une liste (vide) pour les éléments du système solaire
systeme_solaire = []
print("0 - Liste du système solaire (vide) :\n", systeme_solaire)

systeme_solaire.append(soleil) # Ajouter un élément à la liste
print("1 - Ajout du premier élément (n°0) :\n", systeme_solaire)

systeme_solaire.extend(liste_planetes_telluriques) # Ajouter un itérable à la liste
print("2 - Ajout des planètes telluriques :\n", systeme_solaire)
pause()

systeme_solaire.extend(liste_planetes_joviennes)  # Ajouter un itérable à la liste
print("3 - Ajout des planètes joviennes :\n", systeme_solaire)
pause()

print("4 - Liste de toutes les planètes naines :\n", liste_planetes_naines[:])
pause()

CERES = liste_planetes_naines.pop(0) # Extraction d'un élément d'une liste
print("5 - Extraction de la première planète naines", CERES, ":\n", liste_planetes_naines)
pause()

position = systeme_solaire.index("Jupiter")
systeme_solaire.insert(position, CERES)
print("6 - Insertion de", CERES, "entre",
      systeme_solaire[position - 1], "et", systeme_solaire[position + 1], " :", systeme_solaire)
pause()

print("7 - Ajout des planètes naines après", systeme_solaire[-1])
systeme_solaire.extend(liste_planetes_naines)
print("Système Solaire avec les planètes naines :\n", systeme_solaire)
pause()

CHARON = "CHARON".capitalize()
position = systeme_solaire.index(CHARON) #Récupération de la position
print("8 - Suppression de", CHARON, "entre",
      systeme_solaire[position - 1], "et", systeme_solaire[position + 1], ":\n", systeme_solaire)
systeme_solaire.remove(CHARON) # Suppression d'un élément (alternative del systeme_solaire[position])
print("Système Solaire sans", CHARON, ":\n", systeme_solaire)
pause()

print("9 - Liste des planètes du système solaire :")
for i, item in enumerate(systeme_solaire):
    print("\t •", i, "=", item)
pause()

systeme_solaire.sort() # Réordonnancement des éléments (/Alpha-Numérique)
print("10 - Les planètes par ordre aplhabétique (sort) :\n", systeme_solaire)
print("N.B. : Le réordonnancement des planètes est conservé, car une liste est un objet mutable.")
pause()

# Syntaxe avancée : filtrage d'une liste
liste_filtre = [element.upper() for element in systeme_solaire if len(element) <= 5]
print("11 - Les planètes du système solaire composés de 5 lettres maximums :",
      liste_filtre, type(liste_filtre))
pause()

print('_' * 64, "Fin de la démonstration")