class Rekins():
    def __init__(self, klients, veltijums, izmers,materials):
        self.klients = klients
        self.veltijums = veltijums
        self.izmers = izmers
        self.materials = materials

    def izdrukat(self):
        print("Klients:", self.klients)
        print("Veltijums:", self.veltijums)
        print("Izmers:", self.izmers)
        print("Materials:", self.materials)

    def aprekins():
        darba_samaksa = 15
        PVN = 21
        produkta_cena = (veltijuma teksta garums) * 1.2 + (platums/100 * garums/100 * augstums/100) / 3 * materiala
        PVN_summa = (produkta_cena + darba_samaksa)*PVN/100
        rekina_summa = (produkta_cena + darba_samaksa) + PVN_summa

pirmais = Rekins("Anna", "Lai izdodas!", [20,20,20], 3.5)
pirmais.izdrukat()

