class Recept:
    def __init__(self, naam, omschrijving):
        self.__naam = naam
        self.__omschrijving = omschrijving
        self.__ingredient_list = []
        self.__stappen = []
        self.__aantal_personen = 1

    def voeg_ingredient_toe(self, ingredient):
        self.__ingredient_list.append(ingredient)

    def voeg_stap_toe(self, stap):
        self.__stappen.append(stap)

    def get_naam(self):
        return self.__naam

    def get_omschrijving(self):
        return self.__omschrijving
    
    def get_stappen(self):
        return self.__stappen

    def get_aantal_personen(self):
        return self.__aantal_personen

    def set_aantal_personen(self, aantal_personen):
        self.__aantal_personen = aantal_personen
        for ingredient in self.__ingredient_list:
            ingredient.set_hoeveelheid(aantal_personen)

    def get_ingredienten(self, plantaardig=False):
        ingredienten = []

        for ingredient in self.__ingredient_list:
            gekozen_ingredient = ingredient.get_ingredient(plantaardig)
            gekozen_ingredient.set_hoeveelheid(self.__aantal_personen)
            ingredienten.append(gekozen_ingredient)

        return ingredienten

    def bereken_totaal_kcal(self, plantaardig=False):
        totaal = 0

        for ingredient in self.get_ingredienten(plantaardig):
            totaal += ingredient.get_kcal() * self.__aantal_personen

        return totaal
    
    def __str__(self):
        tekst = f"{self.__naam}\n"
        tekst += f"{self.__omschrijving}\n"
        tekst += f"Aantal personen: {self.__aantal_personen}\n\n"

        tekst += "Ingrediënten:\n"
        for ingredient in self.get_ingredienten():
            tekst += f"- {ingredient}\n"

        tekst += "\nBereidingsstappen:\n"
        for i, stap in enumerate(self.__stappen, start=1):
            tekst += f"{i}. {stap}\n"

        return tekst