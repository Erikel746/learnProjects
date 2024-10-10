from Auto import Auto

class ElektroAuto(Auto):
    def __init__(self, marke, baujahr, anzahltueren, batterieladestand):
        super().__init__(marke, baujahr, anzahltueren)
        self.__batterieladestand = batterieladestand

    def get_batterieladestand(self):
        return self.__batterieladestand

    def set_batterieladestand(self, batterieladestand):
        self.__batterieladestand = batterieladestand

    def anzeigen_info(self):
        super().anzeigen_info()
        print(f"Batterieladestand: {self.__batterieladestand}%")
