class Stap:
    def __init__(self, beschrijving):
        self.__beschrijving = beschrijving

    def get_beschrijving(self):
        return self.__beschrijving

    def __str__(self):
        return self.__beschrijving
    