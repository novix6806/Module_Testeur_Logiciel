# Démonstration : Les répétitives
print("Table de Multiplication")
nb = int(input("Indiquer un nombre : "))
# Affichage de la table de multiplication sans répétitives :
print("\n(Sans répétitives)")
print("1 x", nb, "=", 1 * nb)
print("2 x", nb, "=", 2 * nb)
print("3 x", nb, "=", 3 * nb)
print("4 x", nb, "=", 4 * nb)
print("5 x", nb, "=", 5 * nb)
print("6 x", nb, "=", 6 * nb)
print("7 x", nb, "=", 7 * nb)
print("8 x", nb, "=", 8 * nb)
print("9 x", nb, "=", 9 * nb)
print("10 x", nb, "=", 10 * nb)
# Affichage de la table de multiplication avec répétitive while :
print("\n(Avec répétitives While)")
i = 0
while i < 10:
    i += 1
    print(i, "x", nb, "=", i * nb)
 # Fin du bloc itératif
# Affichage de la table de multiplication avec répétitive for…in…range :
print("\n(Avec répétitives For)")
for i in range(10):
    m = i + 1
    print(m, "x", nb, "=", m * nb)
 # Fin du bloc itératif
# Affichage de la table de multiplication avec répétitive for…in…range :
print("\n(Avec répétitives For jusqu'à une limite)")
nb_limite = int(input("On doit s'arrêter lorsque le résultat est égale : ")) 
for i in range(10 + 1):
    print(i, "x", nb, "=", i * nb)
    if i * nb == nb_limite:
        print("Python arrête de calculer !")
        break
 # Fin du bloc itératif
print("\nTable de Multiplication de", nb, "(impaire) :")
for i in range(1, 10 + 1): # Séquencer i de 1 à 10 (inclus)
    if i % 2 == 0: # Est-ce que 'i' est un nombre paire ? 
        continue # Prochaine itération
    print(i, "x", nb, "=", i * nb)
 # Fin du bloc itératif
print("_" * 64, "Fin du programme") # __________ Fin de l'algorithme6
