import mysql.connector
import json
from datetime import datetime
"""
Connection to the server.
The username is root, the password is 1234 and the hostname is localhost
"""


class DbManager:

    def __init__(self):

        self.username = "python_user"
        self.passwd = "python"
        self.host = "localhost"
        self.db = "pimdb"
        self.table = "project_table"

    def connect_db(self):
        try:
            db = mysql.connector.connect(
                user=self.username, passwd=self.passwd, host=self.host, database=self.db)
            print("Successfully connected to database")
            return db
        except Exception as e:
            print(e)
            print("Cant connect to database - check error message above")
            return None

    def run_query(self, query):
        db = self.connect_db()
        my_cursor = db.cursor()
        my_cursor.execute(query)
        return my_cursor.fetchall()

    def update_db(self):
        pass

    def select_all(self):
        query = f"SELECT * FROM {self.db}.{self.table};"
        return self.run_query(query)

    def return_list(self, format_time=True):

        projects = [list(row) for row in self.select_all()]
        if format_time:
            for p in range(len(projects)):
                for i in range(len(projects[p])):
                    if type(projects[p][i]) != int and type(projects[p][i]) != str:
                        projects[p][i] = projects[p][i].strftime(
                            format="%d-%m-%Y")

        return projects

    def return_dict(self, format_time=True):
        project_structure = {}
        # getting all the rows from the query
        projects = [list(row) for row in self.select_all()]

        if format_time:
            for p in range(len(projects)):
                for i in range(len(projects[p])):
                    if type(projects[p][i]) != int and type(projects[p][i]) != str:
                        projects[p][i] = projects[p][i].strftime(
                            format="%d-%m-%Y")

        for i in range(len(projects)):
            project_structure[projects[i][0]] = {  # the id of the project is the primarykey
                'name': projects[i][1],
                'leader': projects[i][2],
                'progress': projects[i][3],
                'start': projects[i][4],
                'estend': projects[i][5],
                'stagedev': projects[i][6],
                'currenttime_stage_days': projects[i][7],
                'current_responsible': projects[i][8],
                'next_responsible': projects[i][9]
            }
        return project_structure

    def __str__(self):
        return f"""SUCCESFULLY CONNECTED TO: {self.host}\nDatabase: {self.db}, Table: {self.table}\nUsername: {self.username}, password: {'*'*len(self.passwd)}"""

    def return_json(self, format_time=True):
        to_json = json.dumps(self.return_dict(format_time), indent=3)
        return to_json


db = DbManager()

print(db.return_list())
