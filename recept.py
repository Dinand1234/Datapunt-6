class Recept:
    def __init__(self, naam, omschrijving):
        self.__naam = naam
        self.__omschrijving = omschrijving
        self.__ingredient_list = []
        self.__stappen = []

    def voeg_ingredient_toe(self, ingredient):
        self.__ingredient_list.append(ingredient)

    def voeg_stap_toe(self, stap):
        self.__stappen.append(stap)

    def get_naam(self):
        return self.__naam

    def get_omschrijving(self):
        return self.__omschrijving

    def get_ingredienten(self):
        return self.__ingredient_list

    def get_stappen(self):
        return self.__stappen

    def __str__(self):
        tekst = f"{self.__naam}\n"
        tekst += f"{self.__omschrijving}\n\n"

        tekst += "Ingrediënten:\n"
        for ingredient in self.__ingredient_list:
            tekst += f"- {ingredient}\n"

        tekst += "\nBereidingsstappen:\n"
        for i, stap in enumerate(self.__stappen, start=1):
            tekst += f"{i}. {stap}\n"

        return tekst