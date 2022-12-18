# imports
import PySimpleGUI as sg
from databas import Databas, Medlem
from display import Display, Popup
from os import mkdir

# Tema
sg.theme('DarkGreen5')

try:
    mkdir('C:\\db')
except FileExistsError:
    print('Fil finns redan')

# Sätt upp och skapa databasen
db = Databas('sqlite:///C:\\db\\database01.db')
db.create_database()

# Initiera displayen/tabellen med hur databasen ser ut nuvarande
data = db.get_all_data()
display1 = Display(data)

# Knapp och sök frames
buttons_frame = [[sg.Button('Lägg till', key='-ADD-'), sg.Button('Ta bort', key='-DEL-')]]
search_frame = [
    [sg.Text('Förnamn'), sg.Input(key='-seek1-', size=(20, 1)), sg.Text('Efternamn'), sg.Input(key='-seek2-', size=(20, 1)), sg.Button('Sök', key='-SEEK-')]
                ]
# layout med text, display/tabell och frames
base_layout = [
    [sg.Text('Medlemsregister', font=('helvetica', 15, 'bold'))],
    [display1.place_display()],
    [sg.Frame('', search_frame), sg.Push(), sg.Frame('', buttons_frame)]
          ]

# fönster
window = sg.Window('Medlemsregister', base_layout)

# sätt upp popups
popup = Popup(window, db, display1)

# fönster loop
while True:
    event, value = window.read()
    if event == sg.WIN_CLOSED:
        break

    # om "lägg till"-knappen trycks kör "lägg till"-funktionen
    if event == '-ADD-':
        popup.add()

    # om "ta bort"-knappen trycks kör "ta bort"-funktionen
    if event == '-DEL-':
        popup.delete()

    # om sök-knappen trycks kör sök-funktionen
    if event == '-SEEK-':

        # sök funktion
        q = db.search(value['-seek1-'], value['-seek2-'])

        # Visa resultat
        display1.update_display(window, q)

# Stäng fönster
window.close()

