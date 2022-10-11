import datetime
import csv

class Rekins():
    def __init__(self,klients,veltijums,izmers,materials):
        self.klients = klients
        self.veltijums = veltijums
        self.izmers = izmers.split(",")
        self.materials = float(materials)
        self.laiks = datetime.datetime.now()
        
        self.aprekins()

    def izdrukat(self):
        print("Klients:",self.klients)
        print("Veltījums:",self.veltijums)
        print("Izmērs:", self.izmers)
        print("Materiāls:",self.materials)
        print("Laiks:",self.laiks)
        print("Apmaksas summa: ", self.aprekins())

    def aprekins(self):
        darba_samaksa = 15
        PVN = 21
        produkta_cena = (len(self.veltijums)) * 1.2 + (int(self.izmers[0])/100 * int(self.izmers[1])/100 * int(self.izmers[2])/100)/ 3 * self.materials
        PVN_summa = (produkta_cena + darba_samaksa)*PVN/100 
        rekina_summa = (produkta_cena + darba_samaksa) + PVN_summa
        return rekina_summa

    def saglabat(self):
        with open('rekini.csv', 'w',encoding="utf-8",newline='') as fails:
            csvwrite = csv.writer(fails)
            csvwrite.writerow(['Klienta vārds','Veltījums','Izmēri','Materiāla cena','Laiks','Cena'])
            csvwrite.writerow([self.klients,self.veltijums,self.izmers,self.materials,self.laiks,self.aprekins()])