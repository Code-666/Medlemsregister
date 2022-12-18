# importera
from sqlalchemy import create_engine, delete, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy import Column, Integer, String, Boolean

# Base klass
Base = declarative_base()

# Databas klass
class Databas:

    def __init__(self, databas_url):

        # Skapa en motor och en session
        self.engine = create_engine(databas_url)
        self.session = sessionmaker(bind=self.engine)()

    # Skapa databas
    def create_database(self):
        Base.metadata.create_all(self.engine)

    # Lägg till data
    def insert(self, data):
        self.session.add(data)
        self.session.commit()
        self.session.close()

    # Ta bort data baserat på ID
    def delete(self, row_id):
        remove = delete(Medlem).where(Medlem.ID == row_id)
        self.session.execute(remove)
        self.session.commit()
        self.session.close()

    # Sök på för- och efternamn
    def search(self, fnamn, enamn):
        data = []
        avgift = ''

        # Fråga på för- och efternamn
        q = self.session.query(Medlem).filter_by(förnamn=fnamn, efternamn=enamn)

        # För varje medlem som har betalat avgift skriv "betalat" om inte skriv "inte betalat"
        for m in q:
            if m.avgift == True:
                avgift = 'betalat'
            elif m.avgift == False:
                avgift = 'inte betalat'

            # Gör allt till en lista så att det ska gå att få upp på displayen/tabellen
            data.append([m.ID, m.förnamn, m.efternamn, m.gatuadress, m.postnummer, m.postadress, avgift])

        return data

    # Få ut all data i databasen
    def get_all_data(self):
        data = []
        avgift = ''

        # Fråga efter all data
        q = self.session.query(Medlem).all()

        # För varje medlem som har betalat avgift skriv "betalat" om inte skriv "inte betalat"
        for m in q:
            if m.avgift == True:
                avgift = 'betalat'
            elif m.avgift == False:
                avgift = 'inte betalat'

            # Gör allt till en lista så att det ska gå att få upp på displayen/tabellen
            data.append([m.ID, m.förnamn, m.efternamn, m.gatuadress, m.postnummer, m.postadress, avgift])

        return data


# Klass för medlemstabell
class Medlem(Base):
    __tablename__ = 'medlem'

    ID = Column(Integer, primary_key=True)
    förnamn = Column(String)
    efternamn = Column(String)
    gatuadress = Column(String)
    postnummer = Column(Integer)
    postadress = Column(String)
    avgift = Column(Boolean)

    def __init__(self, förnamn, efternamn, gatuadress, postnummer, postadress, avgift):
        self.förnamn = förnamn
        self.efternamn = efternamn
        self.gatuadress = gatuadress
        self.postnummer = postnummer
        self.postadress = postadress
        self.avgift = avgift

