#TP Max et Compare

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
    
# Fonction max pour comparer deux nombres et retourner le plus grand    
def max (a, b):
    if a > b:
        return f"Le plus grand nombre est {a}"
    elif a < b:
        return f"Le plus grand nombre est {b}"
    else:
        return "Les deux nombres sont égaux !"
    
# print("_____Comparaison de deux nombres_____")
# print("") # Afficher une ligne vide
# nombre1 = float(input("Saisissez le premier nombre : "))
# nombre2 = float(input("Saisissez le second nombre : "))
# resultat = max(nombre1, nombre2)

# print("") # Afficher une ligne vide
# print("Le résultat de la comparaison est :", resultat)
# print("______Fin du programme_____")
# print("") # Afficher une ligne vide

#Fonction compare pour comparer deux nombres et retourner -1, 0 ou 1
def compare (a, b):
    if a > b:
        return f"la premiere valeur est la plus grande {1}"
    elif a < b:
        return  f"la seconde valeur est la plus grande {-1}"
    else:
        return f"Les deux nombres sont égaux !"
    
# print("_____Comparaison de deux nombres avec compare_____")
# print("") # Afficher une ligne vide
# nombre1 = float(input("Saisissez le premier nombre : "))
# nombre2 = float(input("Saisissez le second nombre : "))
# resultat = compare(nombre1, nombre2)

# print("") # Afficher une ligne vide
# print("Le résultat de la comparaison est :", resultat)
# print("______Fin du programme_____")
# print("") # Afficher une ligne vide

def main(): # Programme Principal

    afficher_info("Bienvenue dans cette démonstration de fonctions de comparaison")
    
    choix = saisir_nombre("Quel est votre choix ?",
        """Demande de saisie d'un entier à l'utilisateur :
        1 - Comparer deux nombres avec la fonction max
        2 - Comparer deux nombres avec la fonction compare""")
        
    if choix == 1:
        print("_____Comparaison de deux nombres avec max_____")
        print("") # Afficher une ligne vide
        nombre1 = float(input("Saisissez le premier nombre : "))
        nombre2 = float(input("Saisissez le second nombre : "))
        resultat = max(nombre1, nombre2)

        print("") # Afficher une ligne vide
        print("Le résultat de la comparaison est :", resultat)
        print("______Fin du programme_____")
        print("") # Afficher une ligne vide
        
    elif choix == 2:
        print("_____Comparaison de deux nombres avec compare_____")
        print("") # Afficher une ligne vide
        nombre1 = float(input("Saisissez le premier nombre : "))
        nombre2 = float(input("Saisissez le second nombre : "))
        resultat = compare(nombre1, nombre2)

        print("") # Afficher une ligne vide
        print("Le résultat de la comparaison est :", resultat)
        print("______Fin du programme_____")
        print("") # Afficher une ligne vide
    else:
        print("Choix inconnu, fin du programme.")
        
main() # Appel du programme principal

print('_' * 64, "Fin de la démonstration")
        