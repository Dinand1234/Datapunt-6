class Ingredient:
    def __init__(self, naam, hoeveelheid, eenheid, kcal, plantaardig_alternatief=None):
        self.__naam = naam
        self.__hoeveelheid = hoeveelheid
        self.__basis_hoeveelheid = hoeveelheid
        self.__eenheid = eenheid
        self.__kcal = kcal
        self.__plantaardig_alternatief = plantaardig_alternatief

    def get_naam(self):
        return self.__naam

    def get_hoeveelheid(self):
        return self.__hoeveelheid

    def get_eenheid(self):
        return self.__eenheid

    def get_kcal(self):
        return self.__kcal

    def get_plantaardig_alternatief(self):
        return self.__plantaardig_alternatief

    def set_hoeveelheid(self, aantal_personen):
        self.__hoeveelheid = self.__basis_hoeveelheid * aantal_personen

    def get_ingredient(self, plantaardig):
        if plantaardig and self.__plantaardig_alternatief is not None:
            return self.__plantaardig_alternatief
        return self

    def __str__(self):
        if self.__hoeveelheid == int(self.__hoeveelheid):
            hoeveelheid_tekst = str(int(self.__hoeveelheid))
        else:
            hoeveelheid_tekst = str(self.__hoeveelheid)

        return f"{hoeveelheid_tekst} {self.__eenheid} {self.__naam} ({self.__kcal} kcal)"