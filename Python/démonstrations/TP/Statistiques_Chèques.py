# # TP 02 Statistiques sur les chèques
# print("______Statistiques sur les chèques______")
# print("") # Afficher une ligne vide

# # Déclaration des variables pour les chèques
# numero_cheque = +1
# cheque_saisi = 0
# somme_cheques = 0.0

# # Déclaration des variables pour les statistiques
# LIMITE_CHEQUES = 200
# moyenne_montant = 0.0
# nombre_cheques_inf_limite = 0
# nombre_cheques_sup_limite = 0
# montant_cheques_inf_limite = 0.0
# montant_cheques_inf_bas = 0.0
# montant_cheques_sup_limite = 0.0
# numero_cheque_inf_limite = 0
# numero_cheque_inf_bas = 0
# numero_cheque_sup_limite = 0


# # Enregistrement du numero et du montant de chaque chèque
# while numero_cheque != 0:
#     numero_cheque = int(input("Saisissez le numéro du chèque ou 0 pour terminer : "))
#     if numero_cheque != 0:
#         montant_cheque = float(input("Saisissez le montant du chèque : "))
#         cheque_saisi +=1
#         somme_cheques += montant_cheque
#         if montant_cheque < LIMITE_CHEQUES:
#             nombre_cheques_inf_limite += 1
#             numero_cheque_inf_limite = numero_cheque
#             if numero_cheque < numero_cheque_inf_limite:
#                 numero_cheque_inf_bas = numero_cheque
                
#             montant_cheques_inf_limite += montant_cheque
#             if montant_cheque < montant_cheques_inf_limite:
#                 montant_cheques_inf_bas = montant_cheque
                
#         elif montant_cheque > LIMITE_CHEQUES:
#             nombre_cheques_sup_limite += 1
#             numero_cheque_sup_limite = numero_cheque
#             montant_cheques_sup_limite += montant_cheque
#             print("")
#             print("Chèque enregistré, passez au suivant")
        
# print("")
# print("_____Statistiques sur les chèques______")        

# if cheque_saisi > 0:
#     moyenne_montant = somme_cheques / cheque_saisi
#     print("Le montant total des chèques est de", somme_cheques, "euros pour un total de", cheque_saisi, "chèques saisis")
#     print("Le montant moyen des chèques est de", moyenne_montant, "euros")
#     print("")
    
# print("Nombre de chèques inférieurs à", LIMITE_CHEQUES, "euros est de : ",nombre_cheques_inf_limite)
# if nombre_cheques_inf_limite > 0:
#     moyenne_montant_inf_limite = montant_cheques_inf_limite / nombre_cheques_inf_limite
#     print("Le montant total des chèques inférieurs à", LIMITE_CHEQUES, "euros est de", montant_cheques_inf_limite, "euros")
#     print("Le montant moyen des chèques inférieurs à", LIMITE_CHEQUES, "euros est de", moyenne_montant_inf_limite, "euros")
#     print("Le numéro du chèque dont le montant est le plus petit est :", numero_cheque_inf_bas)
#     print("le montant du chèque le plus petit est de", montant_cheques_inf_bas, "euros")
#     print("")
    
# print("Nombre de chèques supérieurs à", LIMITE_CHEQUES, "euros est de : ",nombre_cheques_sup_limite)
# if nombre_cheques_sup_limite > 0:
#     moyenne_montant_sup_limite = montant_cheques_sup_limite / nombre_cheques_sup_limite
#     print("Le montant total des chèques supérieurs à", LIMITE_CHEQUES, "euros est de", montant_cheques_sup_limite, "euros")
#     print("Le montant moyen des chèques supérieurs à", LIMITE_CHEQUES, "euros est de", moyenne_montant_sup_limite, "euros")
#     print("Le numéro du dernier chèque supérieur à", LIMITE_CHEQUES, "euros est :", numero_cheque_sup_limite)
#     print("le montant du dernier chèque supérieur à", LIMITE_CHEQUES, "euros est de", montant_cheque, "euros")
#     print("")
    
# print("_________________________Fin du programme")  


# TP 03 - Statistiques Chèques
print("_____Statistiques Chèques_____")

# Niveau Essentiel :
numero_cheque = +1 #  Initialisation de la variable (> 0) pour rentrer au moins une fois dans la boucle
nombre_cheques, total_montant = 0, 0.0

# Niveau Attendu :
LIMITE = 200
nb_inferieur_limite, total_inferieur_limite = 0, 0.0
nb_superieur_limite, total_superieur_limite = 0, 0.0

# statistiques
# Le numéro et le montant du chèque dont le montant est le plus petit.
# Le numéro et le montant du chèque dont le montant est le plus grand.
num_cheque_min = numero_cheque
num_cheque_max = numero_cheque
mnt_min = 0.0
mnt_max = 0.0

while numero_cheque > 0:
    print('_________________________________________________________________')
    numero_cheque = int(input("Quel est le numéro du prochain chèque (0 pour sortir) ? "))
    if numero_cheque > 0:
        montant_cheque = float(input("Quel est son montant (. comme séparateur décimal) : "))
        # Niveau Essentiel : Comptabilisation du nombre et des montants par accumulation
        nombre_cheques += 1
        total_montant += montant_cheque

        # Niveau Attendu : Statistiques
        if num_cheque_min == 1:
            # initialisation min et max au valeur actuelle
            mnt_min = montant_cheque
            num_cheque_min = numero_cheque
            mnt_max = montant_cheque
            num_cheque_max = numero_cheque
            print("TEST ",mnt_min, " ",num_cheque_min, " ", mnt_max, " " , num_cheque_max)
        if mnt_min > montant_cheque:
            mnt_min = montant_cheque
            num_cheque_min = numero_cheque
        if mnt_max < montant_cheque:
            mnt_max = montant_cheque
            num_cheque_max = numero_cheque
        
        # Niveau Attendu : Comptabilisation du nombre et des montants en fonction de la limite
        if montant_cheque < LIMITE:
            nb_inferieur_limite += 1
            total_inferieur_limite += montant_cheque
        else:
            nb_superieur_limite += 1
            total_superieur_limite += montant_cheque
        
        print("C'est bien enregistré, passons au suivant…")

# Affichage du calcul de la saisie
print("Affichage des résultats :____________________________________________")
if nombre_cheques > 0:
    # Niveau Essentiel :
    print(" • Nombre de chèques :", nombre_cheques)
    print(" • Somme des chèques :", total_montant, "€")
    print(" • Moyenne des montants :", (total_montant / nombre_cheques), "€")
    
    # Niveau Attendu :
    print(" - - - - - - - - - - - - - - - - - - - - - - - ")
    print(" • Somme des chèques <", LIMITE,"€ :", total_inferieur_limite, "€ ( nb. =", nb_inferieur_limite, ")")
    print(" • Somme des chèques ≥", LIMITE,"€ :", total_superieur_limite, "€ ( nb. =", nb_superieur_limite, ")")
    print(" • Numéro du chèque : ",num_cheque_min ," qui a le montant min = ", mnt_min)
    print(" • Numéro du chèque : ",num_cheque_max ," qui a le montant max = ", mnt_max)
else:
    print(" # Aucun chèque saisi !")

print("_________________________________Fin du programme")
    
    

    
    