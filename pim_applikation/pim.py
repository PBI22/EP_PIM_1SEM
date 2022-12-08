import pandas as pd
import db # import our database module
from datetime import datetime
import json

"""

pimp.py is a Product Information Management Process module. It contains handling of Product and Project information.

"""

class PimpManager:

    """
    PimManager class for managing the projects and overall project information  
    """

    def __init__(self, projects=db.read_db_file(get_dict=True), from_date="1900-01-01", to_date=datetime.now(), search_key=None, user="admin"):
        self.projects = projects
        self.user = user
        self.from_data = from_date
        self.to_date = to_date
        self.searchkey = search_key

    def get_projects(self):
        return self.projects

    def set_projects(self, projects):
        self.projects = projects

    def save_projects(self):
        db.save_db(projects=self.projects)

    def set_keyword(self, keyword):
        self.searchkey = keyword

    def get_keyword(self):
        return self.searchkey

    def get_from(self):
        return self.from_data

    def set_from(self, from_date):
        self.from_data = from_date

    def get_to(self):
        return self.to_date

    def set_to(self, to_date):
        self.to_date = to_date
        
    def __str__(self):
        return f"Projects in Database:\n {json.dumps(self.projects, indent = 3)}"


class Project:
    pass

test = PimpManager()

#print(test)
print(test.get_projects())