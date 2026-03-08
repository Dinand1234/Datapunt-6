class Ingredient:
    def __init__(self, naam, hoeveelheid, eenheid, kcal, plantaardig_alternatief=None):
        self.__naam = naam
        self.__hoeveelheid = hoeveelheid
        self.__basis_hoeveelheid = hoeveelheid
        self.__eenheid = eenheid
        self.__kcal = kcal
        self.__plantaardig_alternatief = plantaardig_alternatief

    def __str__(self) -> str:
        # Mooier weergeven: 1.0 -> 1
        if self.hoeveelheid == int(self.hoeveelheid):
            hoeveelheid_tekst = str(int(self.hoeveelheid))
        else:
            hoeveelheid_tekst = str(self.hoeveelheid)

        return f"{hoeveelheid_tekst} {self.eenheid} {self.naam}"
        