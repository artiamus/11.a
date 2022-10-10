class Auto():
    def __init__(self,modelis,krasa):
        self.modelis = modelis
        self.krasa = krasa

bmw = Auto(modelis = "XS", krasa = "Sarkana")

print(bmw.modelis)

class Auto():
    def __init__(self, modelis,krasa):
        self.modelis = modelis
        self.krasa = krasa

    def dati(self):
        print(f"modelis ir {self.modelis}, krasa - {self.krasa}")
    
    def krasas_maina(self, jaunaKrasa):
        print(f"Ieprekseja auto krasa - {self.krasa}")
        print(f"Jauna auto krasa - {jaunaKrasa}")

audi = Auto(modelis="Q6", krasa="zila")

audi.dati()
audi.krasas_maina("melna")