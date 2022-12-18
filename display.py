from databas import Medlem
import PySimpleGUI as sg

# Klass för en display i from av en tabell
class Display:

    def __init__(self, data):
        self.data = data

    # placera displayen/tabellen
    def place_display(self):
        head = ['ID', 'Förnamn', 'Efternamn', 'Gatuadress', 'Postnummer', 'Postadress', 'Avgift']
        return [sg.Table(self.data, head, expand_x=True, key='-tab-')]

    # updatera displayen/tabellen
    def update_display(self, window, new_data):
        window['-tab-'].update(new_data)
        window.refresh()

# Popup fönster klass
class Popup:

    def __init__(self, window, db, display):
        self.window = window
        self.db = db
        self.display = display

    def add(self):

        # layout för "lägg till" funktionen
        layout = [
            [sg.Text('Förnamn'), sg.Push(), sg.Input(key='-add1-', size=(20, 1))],
            [sg.Text('Efternamn'), sg.Push(), sg.Input(key='-add2-', size=(20, 1))],
            [sg.Text('Gatuadress'), sg.Push(), sg.Input(key='-add3-', size=(20, 1))],
            [sg.Text('Postnummer'), sg.Push(), sg.Input(key='-add4-', size=(20, 1))],
            [sg.Text('Postadress'), sg.Push(), sg.Input(key='-add5-', size=(20, 1))],
            [sg.Checkbox('Avgift', key='-add6-'), sg.Push(), sg.Button('Lägg till', key='ADD_DATA')]
                  ]

        # fönster för "lägg till" funktionen
        add_window = sg.Window('Lägg till', layout)

        # fönster loop
        while True:
            event, value = add_window.read()
            if event == sg.WIN_CLOSED:
                break

            if event == 'ADD_DATA':

                # Gör ett medlems objekt med input data
                m = Medlem(value['-add1-'],value['-add2-'],value['-add3-'],value['-add4-'],value['-add5-'],value['-add6-'])

                # lägg till objekt i databasen
                self.db.insert(m)

                # uppdatera displayen/tabellen
                self.display.update_display(self.window, self.db.get_all_data())

        add_window.close()

    def delete(self):

        # layout för "ta bort" funktionen
        layout = [
            [sg.Text('Ta bort en medlem med dens ID')],
            [sg.Text('ID'), sg.Input(key='-del1-', size=(20, 1)), sg.Button('Ta bort', key='DEL_DATA')]
                  ]

        # fönster för "ta bort" funktionen
        del_window = sg.Window('Ta bort', layout)

        # fönster loop
        while True:
            event, value = del_window.read()
            if event == sg.WIN_CLOSED:
                break

            if event == 'DEL_DATA':
                # ta bort data med specificerat ID
                self.db.delete(value['-del1-'])

                # uppdatera displayen/tabellen
                self.display.update_display(self.window, self.db.get_all_data())

        del_window.close()

