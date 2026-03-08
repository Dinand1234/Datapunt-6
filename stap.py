class Stap:
    def __init__(self, beschrijving, tip=None):
        self.__beschrijving = beschrijving
        self.__tip = tip

    def get_beschrijving(self):
        return self.__beschrijving

    def __str__(self):
        return self.__beschrijving
    