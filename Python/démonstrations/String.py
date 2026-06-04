# Démonstration : Les chaînes de caractères (str)
NB, SYMB = 56, '_'
print("Démonstration : Les chaînes de caractères (str)".center(2 * NB, SYMB))

pause = lambda: input('\n' + (SYMB * (NB//2)) + "Appuyer sur 'Entrée' pour continuer…\n")

chaine = input("\n=> Saisir une phrase (ou vide si non inspiré) pour continuer : \n").strip() or "Le MERCREDI c'est permis !"
print("chaine (d'origine) = \"%s\" %s" % (chaine, type(chaine)))
# Opérations de mise en forme
print("\tchaine.upper() : %s" % chaine.upper())
print("\tchaine.lower() : %s" % chaine.lower())
print("\tchaine.capitalize() : %s" % chaine.capitalize())
print("\tchaine.chaine.title() : %s" % chaine.title())
phrase = chaine.center(len(chaine) + 10, SYMB)
print("\tphrase = chaine.center(len(chaine) + 10, SYMB) : %s" % phrase)
print("\tphrase.strip(SYMB) : '%s'" % phrase.strip(SYMB)) # la méthode strip() permet d'annuler center()
print("\tchaine.swapcase() : %s" % chaine.swapcase())
pause()

print("\nchaine (rappel) = \"{0}\" {1}\n".format(chaine, type(chaine)))
print("N.B. : Observer que sa valeur n'a pas été modifiée,\n car il s'agit d'un objet non mutable (imutable)")
pause()

print("\nOn peut aussi obtenir des informations détaillés (numériques ou booléennes)")
print("\tchaine (rappel) = \"{}\" {}".format(chaine, type(chaine)))
lettre = input("\n=> Saisissez une lettre présente (de préférence) dans la phrase 'chaine' ci-dessus : ") or 'i' # lettre = 'i' si non renseigné
print("\tlen(chaine) : la chaine mesure {} caractères.".format(len(chaine)))
print("\tlettre = '{}'".format(lettre))
print("\tchaine.count('{chr}') : il y a {num} fois la lettre '{chr}' dans la phrase.".format(chr=lettre, num=chaine.count(lettre)))
print("\tchaine.find('{chr}') : la (première) lettre '{chr}' se trouve à la position {num}.".format(chr=lettre, num=chaine.find(lettre)))
# print("\tchaine.index('{chr}') : la (première) lettre '{chr}' se trouve à la position {num}.".format(chr=lettre, num=chaine.index(lettre))) # Peut provoquer une erreur (raise) si non trouvé
pause()
print("\tchaine.islower() - Est-ce qu'elle est minuscule ?", chaine.islower())
print("\tchaine.isupper() - en Majuscule ?", chaine.isupper())
print("\tchaine.isalnum() - Est-ce qu'elle contient uniquement de l'alpha-numérique ?", chaine.isalnum())
print("\tchaine.isalpha() - ou que de l'alpha ?", chaine.isalpha())
print("\tchaine.istitle() - Est-ce qu'il s'agit d'un Titre ?", chaine.istitle())
print("\tchaine.…(…) <Il  existe encore d'autres méthodes spécifiques à découvrir…>")
pause()

print("/!\\ Petite subtilité : la méthode casefold() se rapproche de la méthode lower(), mais pas que… (observer)")
print("\tchaine.casefold() :", chaine.casefold())
print("Est-ce que 'ß' est équivalent à 'ss' ?\n",
    "'der Fluß'.casefold() == 'der Fluss'.casefold()\n",
     "der Fluß".casefold() == "der Fluss".casefold())

# Par opposition à ces mots en œ, il en existe d’autres dans lesquels o et e se suivent naturellement,
#  et sont prononcés différemment : coexistence, moelleux, coercitif, etc.
#En conclusion, il n’est pas possible d’affirmer que le digramme lié œ n’est pas un graphème unique,
#  car son emploi n’est pas prévisible.
print("Est-ce que 'œ' est équivalent à 'oe' ?\n",
    "'Ma sœur'.casefold() == 'Ma soeur'.casefold()\n",
     'Ma sœur'.casefold() == 'Ma soeur'.casefold()) 
pause()

print(SYMB * NB) # Ligne de séparation

print("\nIl est important de savoir qu'une chaîne de caractères est en réalité un itérable (tuple) de caractères (lettres) :")
print(">for lettre in chaine: print(lettre)")
for lettre in chaine:
    print(lettre)
pause()

# Découpage d'une chaine en liste (split)
print("\nIl est possible de découper une chaîne de caractères,\n afin de la transformer en liste (list) en fonction d'un séparateur via la méthode split() :")

semaine = "lundi, mardi, mercredi, jeudi, vendredi"
print("\nsemaine =", semaine, type(semaine))

SEPARATEUR = ', '
print("On remarque les caractères qui séparent chaque élément :")
print("SEPARATEUR = '{}'".format(SEPARATEUR))

liste_jours = semaine.split(SEPARATEUR)
print("liste_jours = semaine.split(SEPARATEUR)\n", liste_jours, type(liste_jours))
pause()

liste_jours.extend(("samedi", "dimanche"))
liste_jours = [jour.capitalize() for jour in liste_jours] # Mise en majuscule de la première lettre de chaque élément de la liste
print("Ajout des 2 jours du week-end, et première lettre majuscule :\n", "liste_jours = ", liste_jours)
pause()

print("\nDe même, il est possible de transformer une liste (list) en une chaîne de caractères (str),\n à partir d'un séparateur (str) via la méthode join() :")
semaine = SEPARATEUR.join(liste_jours) # Conversion d'une liste en chaine de caractère (join)
print("semaine = SEPARATEUR.join(liste_jours) :\n \"{}\"".format(semaine))
pause()

print("Fin de la démonstration".center(NB, SYMB))