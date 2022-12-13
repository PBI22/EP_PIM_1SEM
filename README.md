# Produkt Information Management System

Dette eksamensprojekt har til formål at udvikle et generisk produktinformation management system (PIM), der gør det nemt at opbevare, søge og administrere information om produkter under udviklingen. Systemet vil fokusere på at understøtte produktudviklingsprocessen fra designfasen til salgsprototypen gennem tre hovedfaser: design, konstruktion og prototype.

## Funktioner

- Gemme og administrere produktinformation i en database
- Søge efter produkter ved navn, kategori osv.
- Redigere eksisterende produktinformation
- Filtrere produktlisten efter specifikke kriterier
- En grafisk brugergrænseflade (GUI) til at bearbejde data´en. 

## Teknologier

- Databasestruktur: MySQL
- Applikationsudvikling: Python
- GUI-udvikling: dearpygui

## Installation og brug

For at installere og bruge dette system skal du have Python 3 og en MySQL database. 

Du skal bruge følgende biblioteker:
mysql-connector-python
dearpygui
Disse kan installeres ved hjælp af `pip -r requirements.txt`.

1. Klon dette repo til din computer
2. Tilkobl dig MySQL databasen ved at ændre db_login listen i `pim.py`
3. Kør applikationen ved hjælp af kommandoen `python gui_main.py`


## Dokumentation

Se [dokumentationen](docs/pim-docs.pdf) for yderligere detaljer om systemets arkitektur, kodestruktur og brug. // Kommer
