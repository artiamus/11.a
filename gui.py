import PySimpleGUI as sg

sg.theme('DarkAmber')

layout = [[sg.Text('Nospied'),sg.Button('Skeres')],
[sg.Text('',key='-LEMUMS-')],
[sg.Button('Neaizvert')],
[sg.Button('Aizvert')]]

window = sg.Window('Spele', layout)

while True:
    event, values = window.read()
    if event == 'Skeres':
        window['-LEMUMS-'].update('Izvele: Skeres')
    if event == 'Aizvert':
        break

window.close()