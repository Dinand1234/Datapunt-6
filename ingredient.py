class Ingredient:
    def __init__(self, naam: str, hoeveelheid: float, eenheid: str):
        self.naam = naam
        self.hoeveelheid = hoeveelheid
        self.eenheid = eenheid

    def __str__(self) -> str:
        # Mooier weergeven: 1.0 -> 1
        if self.hoeveelheid == int(self.hoeveelheid):
            hoeveelheid_tekst = str(int(self.hoeveelheid))
        else:
            hoeveelheid_tekst = str(self.hoeveelheid)

        return f"{hoeveelheid_tekst} {self.eenheid} {self.naam}"
    