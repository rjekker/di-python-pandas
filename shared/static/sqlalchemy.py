from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///personen.sqlite', echo=False)
# maak 1 sessionfactory per python programma/db connectie
session_factory = sessionmaker(bind=engine)

class Persoon(Base):
    __tablename__ = "persoon"  # DB tabelnaam

    id = Column(Integer, primary_key=True)
    naam = Column(String)
    leeftijd = Column(Integer)
    woonplaats = Column(String)


def nieuwe_invoer():
    Base.metadata.create_all(engine)

    session = session_factory()
    alle_personen = session.query(Persoon).all()
    print("Er zitten nu ", len(alle_personen), " personen in de db")

    for p in alle_personen:
        print(p.naam, p.leeftijd, p.woonplaats)

    naam = input("Geef een naam? ")
    if not naam:
        return
    leeftijd = int(input("Geef een leeftijd? "))
    woonplaats = input("Geef een woonplaats? ")

    p = Persoon(naam=naam, leeftijd=leeftijd, woonplaats=woonplaats)
    session.add(p)
    session.commit()


def verwijderen():
    naam = input("Wie zullen we eens verwijderen? ")
    session = session_factory()
    personen = session.query(Persoon).filter(Persoon.naam == naam)

    print("de volgende personen zijn gevonden:")
    for p in personen:
        print(p.naam, p.leeftijd, p.woonplaats)
        session.delete(p)

    antwoord = input("Weet u het zeker? ")
    if antwoord == "j":
        print("personen worden verwijderd")
        session.commit()
    else:
        print("operatie afgebroken")
        session.rollback()



if __name__=="__main__":
    while True:
        keuze = input("waar heeft u vandaag zin in? Type n voor nieuw en v voor verwijderen")
        if keuze == "n":
            nieuwe_invoer()
        elif keuze == "v":
            verwijderen()
        else:
            print("dat is geen geldige keuze. Doei.")
            break
