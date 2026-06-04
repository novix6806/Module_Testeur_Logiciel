if __package__ in (None, ""):
    import sys
    from pathlib import Path

    sys.path.append(str(Path(__file__).resolve().parent.parent))
    from Modele.Vehicule import Voiture
else:
    from .Vehicule import Voiture

une_voiture = Voiture()
une_voiture.set_marque ( "Citroën")
une_voiture.set_modele ("Cactus")
une_voiture.set_vitesse_max(210)
une_voiture.set_nb_portes (5)
une_voiture.set_nb_places (5)
une_voiture.set_couleur ("Grise")
une_voiture.set_peinture("Métallisée")
une_voiture.puissance = 80

print(" • La voiture est neuve :\n\t{}\n".format(une_voiture))

une_voiture.demarrer()
print(" • La voiture est démarrée :\n\t{}\n".format(une_voiture))

une_voiture.accelerer(6)
print(" • La voiture accélère :\n\t{}\n".format( une_voiture))

une_voiture.accelerer(vitesse_limite  :=  80)
print(" • La voiture accélère jusqu'à atteindre la vitesse de {} km :\n\t{}\n".format(vitesse_limite, une_voiture))

une_voiture.freiner(vitesse_limite  :=  30)
print(" • La voiture ralentit jusqu'à la vitesse de {} km :\n\t{}\n".format(vitesse_limite, une_voiture))

une_voiture.freiner()
print(" • La voiture freine jusqu'à s'arrêter :\n\t{}\n".format(une_voiture))

une_voiture.arreter()
print(" • La voiture coupe son moteur :\n\t{}\n".format(une_voiture))