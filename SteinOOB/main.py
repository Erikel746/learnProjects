from ElektroAuto import ElektroAuto
from VerbrennerAuto import VerbrennerAuto

def main():
    elektro_auto = ElektroAuto("Tesla", 2022, 5, 100)
    verbrenner_auto = VerbrennerAuto("Volkswagen", 2023, 3, 50)

    print("ElektroAuto Info:")
    elektro_auto.anzeigen_info()

    print("\nVerbrennerAuto Info:")
    verbrenner_auto.anzeigen_info()


if __name__ == "__main__":
    main()
