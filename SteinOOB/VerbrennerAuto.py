from Auto import Auto

class VerbrennerAuto(Auto):
    def __init__(self, marke, baujahr, anzahltueren, tankinhalt):
        super().__init__(marke, baujahr, anzahltueren)
        self.__tankinhalt = tankinhalt

    def get_tankinhalt(self):
        return self.__tankinhalt

    def set_tankinhalt(self, tankinhalt):
        self.__tankinhalt = tankinhalt

    def anzeigen_info(self):
        super().anzeigen_info()
        print(f"Tankinhalt: {self.__tankinhalt} l")
