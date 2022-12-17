import PySimpleGUI as sg
import gui

data1 = [['a', 1]]
data2 = [['b', 2]]
head = ['Name', 'ID']

popup = gui.Popup()

base_layout = [
    popup.search_popup(),
    [sg.Button('Lägg till', key='open-add'), sg.Button('Ta bort', key='del-add')],
    [sg.Table(data1, head, expand_x=True, key='-tab-')]
               ]

window = sg.Window('register', base_layout)

while True:

    event, value = window.read()

    if event == sg.WIN_CLOSED:
        break

window.close()