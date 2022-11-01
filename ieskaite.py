#1 uzdevums

from PIL import Image

def thumbnail(nosaukums,izmers):
    with Image.open(nosaukums) as img:
        izmeers = izmers.split(',')
        img.thumbnail((int(izmeers[0]),int(izmeers[1])))
        img.save('bilde.png',img.format)

thumbnail('emoji.png','100,100')

#2 uzdevums

import PySimpleGUI as gui
import random

def CPUIzvele():
    varianti=['Akmens','Skeres','Papirs']
    izveele = random.choice(varianti)
    return izveele


gui.theme('DarkAmber')


layout = [[gui.Text('Izvelaties Akmens, Skeres vai Papirs:')],
[gui.Button('Akmens',key='rock',size=(10,5)),gui.Button('Skeres',key='scissors',size=(10,5)),gui.Button('Papirs',key='paper',size=(10,5))],
[gui.Text('Jusu Izvele: ',key='your_choice')],
[gui.Text('Datora Izvele: ',key='cpu_choice')],
[gui.Text('',key='-STATUS-',size=(200,None),justification='c',font=('Arial',32, 'bold'))]]

window = gui.Window('RockPaperScissors',layout,size=(300,250),element_justification='c')

while True:
    event, values = window.read()
    if event == gui.WIN_CLOSED:
        break

    if event == 'rock':
        cpu = CPUIzvele()
        window['cpu_choice'].update('Datora Izvele: '+cpu)
        window['your_choice'].update('Jusu Izvele: '+'Akmens')
        if cpu == 'Papirs':
            window['-STATUS-'].update('DEFEAT')
        if cpu == 'Akmens':
            window['-STATUS-'].update('DRAW')
        if cpu == 'Skeres':
            window['-STATUS-'].update('VICTORY!') 
    if event == 'scissors':
        cpu = CPUIzvele()
        window['cpu_choice'].update('Datora Izvele: '+cpu)
        window['your_choice'].update('Jusu Izvele: '+'Skeres')
        if cpu == 'Papirs':
            window['-STATUS-'].update('VICTORY!')
        if cpu == 'Akmens':
            window['-STATUS-'].update('DEFEAT')
        if cpu == 'Skeres':
            window['-STATUS-'].update('DRAW') 
    if event == 'paper':
        cpu = CPUIzvele()
        window['cpu_choice'].update('Datora Izvele: '+cpu)
        window['your_choice'].update('Jusu Izvele: '+'Papirs')
        if cpu == 'Papirs':
            window['-STATUS-'].update('DRAW')
        if cpu == 'Akmens':
            window['-STATUS-'].update('VICTORY!')
        if cpu == 'Skeres':
            window['-STATUS-'].update('DEFEAT') 
        
        

window.close()

#3 uzdevums

class Ballite():
    def __init__(self,dekoracijas, ciemini, ediens, vel_davanas):
        self.dekoracijas = dekoracijas
        self.ciemini = ciemini
        self.ediens = ediens
        self.velDavanas = vel_davanas

    def pirkumi(self):
        print('\nNepieciešams nopirkt sekojošās dekorācijas:')
        for i in self.dekoracijas:
            print(i)
        print('\nNepieciešams nopirkt sekojošos ēdienus:')
        for i in self.ediens:
            print(i)

    def Davanas(self):
        print('\nVēlamais dāvanu saraksts:')
        for i in self.velDavanas:
            print(i)

dzD = Ballite(["Baloni","Virtene","Salvetes"],["Anna","Pēteris","Zeltīte","Valters"],["Kartupeļi","Gurķi","Burkāni","Kūka","Sula"],["Grāmata","Krājkase","Termokrūze"])
print(dzD.ediens)
dzD.pirkumi()
dzD.Davanas()
