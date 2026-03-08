from recept import Recept
from ingredient import Ingredient
from stap import Stap


def toon_recepten_overzicht(recepten):
    print("=== Receptenoverzicht ===")
    for i, recept in enumerate(recepten, start=1):
        print(f"{i}. {recept.get_naam()}")


def kies_recept(recepten):
    while True:
        keuze = input("\nKies een receptnummer: ")

        if not keuze.isdigit():
            print("Voer een geldig nummer in.")
            continue

        keuze = int(keuze)

        if 1 <= keuze <= len(recepten):
            return recepten[keuze - 1]

        print("Dit receptnummer bestaat niet.")