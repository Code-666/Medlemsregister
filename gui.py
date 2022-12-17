import PySimpleGUI as sg

class Display:

    def __init__(self, window, key):
        self.window = window
        self.key = key

    def update_display(self, data):
        self.window[self.key].update(data)
        self.window.refresh()

class Popup:

    def add_popup(self):
        popup = [
            [sg.Text('Förnamn'), sg.Push(), sg.Input()],
            [sg.Text('Efternamn'), sg.Push(), sg.Input()],
            [sg.Text('Gatuadress'), sg.Push(), sg.Input()],
            [sg.Text('Postnummer'), sg.Push(), sg.Input()],
            [sg.Text('Postadress'), sg.Push(), sg.Input()],
            [sg.Checkbox('Avgift'), sg.Push(), sg.Button('Lägg till')]
                 ]
        return popup

    def del_popup(self):
        popup = [
            [sg.Text('Ta bort en medlem med dens ID')],
            [sg.Text('ID'), sg.Input(), sg.Button('Ta bort')]
                 ]
        return popup

    def search_popup(self):
        popup = [
            [sg.Text('Förnamn'), sg.Input(size=(10, 1)), sg.Text('Efternamn'), sg.Input(size=(10, 1)), sg.Button('Sök')]
                 ]
        return popup

