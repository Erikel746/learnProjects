from Fahrzeug import Fahrzeug

class Auto(Fahrzeug):
    def __init__(self, marke, baujahr, anzahltueren):
        super().__init__(marke, baujahr)
        self.__anzahltueren = anzahltueren

    def get_anzahltueren(self):
        return self.__anzahltueren

    def set_anzahltueren(self, anzahltueren):
        self.__anzahltueren = anzahltueren

    def anzeigen_info(self):
        super().anzeigen_info()
        print(f"Anzahl der Türen: {self.__anzahltueren}")
