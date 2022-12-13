import mysql.connector # MySQL Python bibliotek
from datetime import date #date til håndtering af dato format fra MySQL databasen


class DbManager:
    """
    PIMGO Database Manager
    Database class to handle database connection and queries with MySQL Database.
    class DbManager(username, password, host, database_name , *optional[table_route])
    """
    # DbManager konstruktør tager 5 argumenter. table_route er dog optionel )
    def __init__(self, username, passwd, host, db_name, table_route=None):

        self.username = username
        self.passwd = passwd
        self.host = host
        self.db_name = db_name
        self.loaded_db = self.connect_db()
        self.tables = self.set_tables()
        self.table_route = table_route # Sætter et hierarki til tabellerne, til brug i Pim Class
        self.database_map = self.map_database()  # Udtrækker hele databasen og gemmer som en dictonary - gør det også nemt at gemme i JSON format.

    def connect_db(self):
        try:
            db = mysql.connector.connect(user=self.username, passwd=self.passwd, host=self.host, database=self.db_name)
            return db
        except Exception as e:
            print("Cant Connect to Database - Error: ", e)
            return None

    # Kør Query og returnere rows
    def run_query(self, query):
        db = self.loaded_db
        my_cursor = db.cursor()
        my_cursor.execute(query)
        return my_cursor.fetchall()

    # Kør query med commit - bruges til at lave ændringer i databasen
    def update_query(self, query):
        db = self.loaded_db
        my_cursor = db.cursor()
        my_cursor.execute(query)
        db.commit()

    # Kører Query og returnere rows + columns names
    def run_custom_query(self, query):
        db = self.loaded_db
        my_cursor = db.cursor()
        my_cursor.execute(query)
        column_names = [column[0] for column in my_cursor.description]
        return my_cursor.fetchall(), column_names

    #Henter alle Tables i den tilkoblet database og returnere en liste med dem.
    def set_tables(self):
        query = "SHOW TABLES;"
        table_list = [table[0] for table in self.run_query(query)]
        return table_list

    #Henter listen med alle tabeller i objektet.
    def get_tables(self):
        return self.tables

    #Sætter tabelrækkefølge
    def set_table_route(self, list_of_tables):
        self.table_route = list_of_tables  # fx. ['portfolio','project','product','design','construction','prototype']

    #Henter tabelrækkefølge
    def get_table_route(self):
        return self.table_route

    #Returnere alle kolonner fra en angivet tabel.
    def set_columns(self, table):
        query = f"SHOW COLUMNS FROM {table};"
        return self.run_query(query)

    #Returnere alle kolonner fra en angivet tabel, udfra vores database_map(dictonary)  -> Denne bør udfases helt af overstående set_columns
    def get_columns(self, table):
        first_item = next(iter(self.database_map[self.db_name][table]))
        return [column for column in self.database_map[self.db_name][table][first_item].keys()]

    #Henter data fra en kolonne i en tabel og returnere denne (via. database_map )
    def get_column_data(self, table, column):
        data = self.database_map[self.db_name][table]
        return [data[row][column] for row in data.keys()]

    #Bygger dictonary af en tabel. format_time ændrer datoformat fra 2022-10-15 -> 15-10-2022
    def build_dict(self, table, format_time=True):
        columns = self.set_columns(table)
        column_names = [column[0] for column in columns]
        data = self.run_query(f"SELECT * FROM {table};")
        data_dict = {}
        for row in data:
            row_dict = {}
            for i, column in enumerate(column_names):
                if format_time and isinstance(row[i], date):
                    row_dict[column] = row[i].strftime(
                        format="%d-%m-%Y")  # Konvertere MySQL dato(YYYY-MM-DD) til dansk format(DD-MM-YYYY)
                else:
                    row_dict[column] = row[i]
            data_dict[row_dict["id"]] = row_dict
        return data_dict
    # mapper hele databasen via. build_dict . Ved import af json bibliotek, kan denne printe/returneres i letlåselig json og evt. gemmes/bruges loaktl
    def map_database(self):

        data_dict = {self.db_name: {}}
        table_list = self.table_route if self.table_route else self.tables
        for table in table_list:
            data_dict[self.db_name][table] = self.build_dict(table)  # build dict for each table

        return data_dict
        # return json.dumps(data_dict, indent=3)
    #printer oplysninger om DbManager, hvis objektet printes
    def __str__(self):
        return f"""SUCCESFULLY CONNECTED TO: {self.host}\nDatabase: {self.db_name}, Table: {self.tables}\nUsername: {self.username}, password: {'*' * len(self.passwd)}"""
