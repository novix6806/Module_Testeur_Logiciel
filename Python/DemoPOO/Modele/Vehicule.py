class Voiture:
    """Classe de modélisation pour gérer les véhicules de type Voiture"""

    def  __init__(self):
        """Constructeur (unique) de la classe Voiture"""
        self.__marque = "générique"
        self.__modele = "inconnu"
        self.__vitesse = 0.0
        self.__vitesse_max = 130
        self.__nb_portes = 3
        self.__nb_places = 4
        self.__couleur = "Blanche"
        self.__peinture = "Brillante"
        self.__puissance = 0
        self.__etat = "ARRET"
        
    def __str__(self):
        """Affichage des membres de l'objet avec les valeurs associées."""
        return "{obj.__class__} {obj.__dict__}".format(obj=self)
    
    def get_marque(self):
        return self.__marque
    
    def set_marque(self, value):
        self.__marque = value
            
    def get_modele(self):
        return self.__modele
        
    def set_modele(self, value):
        self.__modele = value

    def get_vitesse(self):
        return self.__vitesse

    def set_vitesse(self, value):
        if value < 0:
            value = 0.0  # Pas de vitesse négative.
        self.__vitesse = value

    def get_vitesse_max(self):
        return self.__vitesse_max

    def set_vitesse_max(self, value):
        if value <= 0:
            value = 1  # Pas de valeur négative ou nulle.
        self.__vitesse_max = value

    def get_nb_portes(self):
        return self.__nb_portes

    def set_nb_portes(self, value):
        if value < 0:
            value = 0  # Pas de valeur négative
        self.__nb_portes = value

    def get_nb_places(self):
        return self.__nb_places

    def set_nb_places(self, value):
        if value < 0:
            value = 0  # Pas de valeur négative
        self.__nb_places = value

    def get_couleur(self):
        return self.__couleur

    def set_couleur(self, value):
        self.__couleur = str(value).lower()  # Mise en minuscule

    def get_peinture(self):
        return self.__peinture

    def set_peinture(self, value):
        self.__peinture = str(value).lower()  # Mise en minuscule
        
    @property
    def puissance(self):
        return self.__puissance

    @puissance.setter
    def puissance(self, value: int):
        print("Set Puissance")
        if value < 0:
            value = 0  # Pas de valeur négative
        self.__puissance = value

    @property
    def etat(self):
        return self.__etat

    def _set_etat(self, value: str):
        """Mutateur pour modifier l'état de la voiture,
        uniquement depuis l'intérieur de l'objet,
        en aucun cas il ne devrait être envisagé de modifier celui-ci
        depuis l'extérieur de la classe."""
        self.__etat = str(value).upper()  # Mise en majuscule

    def demarrer(self):
        """Action de démarrage de la voiture"""
        if self.etat in ("ARRET", "STOP"):
            self._set_etat("DEMARRÉ")
            self.__vitesse = 0

    def arreter(self):
        """Action d'arrêt de la voiture"""
        if self.etat in ("DEMARRÉ", "ARRET", "STOP"):
            self._set_etat("ARRET")

    def accelerer(self, vitesse_cible=0):
        """Action d'accélération à une vitesse spécifiée en paramètre :
        • vitesse_cible en km/h."""
        if self.etat != "ARRET" and vitesse_cible > self.__vitesse:
            if vitesse_cible <= self.__vitesse_max:
                self.__vitesse = vitesse_cible
            else:
                self.__vitesse = self.__vitesse_max

    def freiner(self, vitesse_cible=0):
        """Action de freinage jusqu'à une certaine vitesse :
        • duree en sec.
        • itesse_cible en km/h."""
        if self.etat != "ARRET" and vitesse_cible < self.__vitesse:
            if vitesse_cible > 0:
                self.__vitesse = vitesse_cible
            else:
                self.__vitesse = 0
                self._set_etat("ARRET")