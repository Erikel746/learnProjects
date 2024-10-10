class Fahrzeug:
    def __init__(self, marke, baujahr):
        self.__marke = marke
        self.__baujahr = baujahr

    def get_marke(self):
        return self.__marke

    def get_baujahr(self):
        return self.__baujahr

    def set_marke(self, marke):
        self.__marke = marke

    def set_baujahr(self, baujahr):
        self.__baujahr = baujahr

    def anzeigen_info(self):
        print(f"Marke: {self.__marke}, \nBaujahr: {self.__baujahr}")
