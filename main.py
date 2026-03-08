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

def vraag_aantal_personen():
    while True:
        aantal = input("Voor hoeveel personen is het recept? ")

        if aantal.isdigit() and int(aantal) > 0:
            return int(aantal)

        print("Foutieve invoer.")


def vraag_plantaardig():
    while True:
        keuze = input("Wil je de plantaardige versie indien mogelijk? (ja/nee) ").lower()

        if keuze == "ja":
            return True
        if keuze == "nee":
            return False

        print("Foutieve invoer.")


def toon_recept(recept, plantaardig):
    print(f"\n{recept.get_naam()}")
    print(recept.get_omschrijving())
    print(f"Aantal personen: {recept.get_aantal_personen()}\n")

    print("Ingrediënten:")
    for ingredient in recept.get_ingredienten(plantaardig):
        print(f"- {ingredient}")

    print("\nBereidingsstappen:")
    for i, stap in enumerate(recept.get_stappen(), start=1):
        print(f"{i}. {stap}")

    print(f"\nTotaal kcal: {recept.bereken_totaal_kcal(plantaardig)}")

def main():
    recepten = []

    recept1 = Recept("Kip Kerrie", "Kip kerrie zonder pakjes en zakjes")
    recept1.voeg_ingredient_toe(Ingredient("kipfilet", 150, "gram", 165, Ingredient("vegan kipstukjes", 150, "gram", 180)))
    recept1.voeg_ingredient_toe(Ingredient("rijst", 75, "gram", 270))
    recept1.voeg_ingredient_toe(Ingredient("sperziebonen", 100, "gram", 35))
    recept1.voeg_ingredient_toe(Ingredient("ui", 0.5, "stuk", 20))
    recept1.voeg_ingredient_toe(Ingredient("knoflook", 1, "teen", 5))
    recept1.voeg_ingredient_toe(Ingredient("kerriepoeder", 1, "theelepel", 10))
    recept1.voeg_ingredient_toe(Ingredient("kookroom", 75, "ml", 150, Ingredient("plantaardige kookroom", 75, "ml", 130)))
    recept1.voeg_ingredient_toe(Ingredient("olie", 1, "eetlepel", 120))

    recept1.voeg_stap_toe(Stap("Kook de rijst volgens de aanwijzingen op de verpakking."))
    recept1.voeg_stap_toe(Stap("Kook de sperziebonen beetgaar in een pan met water.", "Voeg een snuf zout toe voor extra smaak."))
    recept1.voeg_stap_toe(Stap("Snijd de kipfilet in blokjes en snipper de ui en knoflook fijn."))
    recept1.voeg_stap_toe(Stap("Verhit de olie in een pan en bak de kip rondom gaar."))
    recept1.voeg_stap_toe(Stap("Voeg de ui, knoflook en kerriepoeder toe en bak kort mee."))
    recept1.voeg_stap_toe(Stap("Voeg de kookroom toe en laat het geheel even zachtjes pruttelen.", "Laat de saus niet te hard koken."))
    recept1.voeg_stap_toe(Stap("Serveer met de rijst en sperziebonen."))

    recepten.append(recept1)

    recept2 = Recept("Gehakt quiche met paprika", "Een heerlijke quiche met gehakt en paprika.")
    recept2.voeg_ingredient_toe(Ingredient("bladerdeeg", 3, "plakken", 240))
    recept2.voeg_ingredient_toe(Ingredient("rundergehakt", 125, "gram", 313, Ingredient("vegan gehakt", 125, "gram", 250)))
    recept2.voeg_ingredient_toe(Ingredient("paprika", 0.5, "stuk", 15))
    recept2.voeg_ingredient_toe(Ingredient("ui", 0.5, "stuk", 20))
    recept2.voeg_ingredient_toe(Ingredient("ei", 1, "stuk", 80, Ingredient("lijnzaad-ei", 1, "stuk", 55)))
    recept2.voeg_ingredient_toe(Ingredient("kookroom", 50, "ml", 100, Ingredient("plantaardige room", 50, "ml", 85)))
    recept2.voeg_ingredient_toe(Ingredient("geraspte kaas", 30, "gram", 110, Ingredient("vegan geraspte kaas", 30, "gram", 90)))
    recept2.voeg_ingredient_toe(Ingredient("olie", 1, "eetlepel", 120))

    recept2.voeg_stap_toe(Stap("Verwarm de oven voor op 200 graden."))
    recept2.voeg_stap_toe(Stap("Bekleed een kleine ovenschaal of quichevorm met het bladerdeeg."))
    recept2.voeg_stap_toe(Stap("Snipper de ui en snijd de paprika in blokjes."))
    recept2.voeg_stap_toe(Stap("Bak het gehakt rul in een pan met olie.", "Gebruik een houten lepel om het gehakt los te maken."))
    recept2.voeg_stap_toe(Stap("Voeg de ui en paprika toe en bak kort mee."))
    recept2.voeg_stap_toe(Stap("Klop het ei los met de kookroom."))
    recept2.voeg_stap_toe(Stap("Verdeel het gehaktmengsel over de bodem en schenk het eimengsel eroverheen."))
    recept2.voeg_stap_toe(Stap("Bestrooi met geraspte kaas en bak de quiche in ongeveer 25 minuten goudbruin."))

    recepten.append(recept2)

    recept3 = Recept("Yoghurt ontbijt met banaan en havermout", "Een snel en gezond ontbijt voor 1 persoon.")
    recept3.voeg_ingredient_toe(Ingredient("yoghurt", 200, "ml", 120, Ingredient("sojayoghurt", 200, "ml", 100)))
    recept3.voeg_ingredient_toe(Ingredient("havermout", 40, "gram", 150))
    recept3.voeg_ingredient_toe(Ingredient("banaan", 1, "stuk", 105))
    recept3.voeg_ingredient_toe(Ingredient("honing", 1, "theelepel", 20, Ingredient("agavesiroop", 1, "theelepel", 18)))
    recept3.voeg_ingredient_toe(Ingredient("kaneel", 1, "snufje", 2))

    recept3.voeg_stap_toe(Stap("Doe de yoghurt in een kom."))
    recept3.voeg_stap_toe(Stap("Roer de havermout door de yoghurt.", "Laat het 5 minuten staan voor een zachtere structuur."))
    recept3.voeg_stap_toe(Stap("Snijd de banaan in plakjes en voeg deze toe."))
    recept3.voeg_stap_toe(Stap("Maak het af met honing en een snufje kaneel."))

    recepten.append(recept3)

    toon_recepten_overzicht(recepten)
    gekozen_recept = kies_recept(recepten)

    print("\n=== Gekozen recept ===")
    print(gekozen_recept)


if __name__ == "__main__":
    main()