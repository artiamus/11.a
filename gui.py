import PySimpleGUI as gui
import kushka
from kushka import Rekins

gui.theme('DarkAmber')

laditeLayout = [[gui.Text('Ievadi Vardu')],
[gui.InputText('',key='Vards'),
gui.Text('',key='-DATI-')],
[gui.Text('Ievadi Veltijumu')],
[gui.InputText('',key='Veltijums')],
[gui.Text('Ievadi Izmeru (platums/garums/augstums)')],
[gui.InputText('',key='Izmers')],
[gui.Text('Ievadi Materiala Cenu')],
[gui.InputText('',key='Materials'),
gui.Button('Aprekinat',key='Aprekins')]]

window = gui.Window('Rekins',laditeLayout, size=(500,250),finalize=True)

while True:
    event, values = window.read()
    if event == 'Aprekins':
        print('Poga Nospiesta')
        dati = Rekins(values['Vards'],values['Veltijums'],values['Izmers'],values['Materials'])
        window['-DATI-'].update('Klients: '+values['Vards']+'\nVeltijums: '+values['Veltijums']+'\nIzmers: '+values['Izmers']+'\nMateriala Cena: '+values['Materials']+'\nLaiks: '+str(dati.izdrukat()[0])+'\nSumma: '+str(dati.izdrukat()[1]))
    if event == gui.WIN_CLOSED:
        break

window.close()