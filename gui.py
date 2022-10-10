import PySimpleGUI as sg

sg.theme('DarkAmber')

layout = [[sg.Text('Nospied!'),sg.Button('Skeres'),sg.Button('Akmens'),sg.Button('Papirs')],
[sg.Text('',key='-LEMUMS-')],
[sg.Text('Vards'),sg.InputText()],
[sg.Button('Neaizvert')],
[sg.Button('Aizvert')]]

window = sg.Window('Spele',layout)

while True:
    event, values = window.read()
    if event == 'Skeres':
        window['-LEMUMS-'].update('Izvele: Skeres')
    if event == 'Akmens':
        window['-LEMUMS-'].update('Izvele: Akmens')
    if event == 'Papirs':
        window['-LEMUMS-'].update('Izvele: Papirs')
    if event == 'Neaizvert':
        vards = values[0]
        window['-LEMUMS-'].update(vards)
    if event == 'Aizvert':
        break

window.close()