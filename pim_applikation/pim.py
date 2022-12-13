from db import DbManager # import our database module


"""

pim.py is a Product Information Management Process module. It contains handling of Product and Project information.

"""
# Predefinerede til brug i DbManager
table_route = ["portfolio", "project", "product", "design", "construction", "prototype","employee"]
db_login = ["python_user", "python", "localhost", "pim_generic"]

# Custom SQL Queries til Data Magi - Bør implementeres i en database eller anden lokation
custom_sql = {"Q1": """
SELECT d.name, d.specifications, d.beskrivelse, IFNULL(d.start_date,'Ikke startet') as start_date, IFNULL(d.end_date,'Ikke afsluttet') as end_date, IFNULL(end_date-start_date,CURRENT_DATE()-start_date) as 'Antal dage i fase',CONCAT(employee.name," (",employee.role,") ") AS 'Manager' FROM design as d
JOIN employee ON employee.id = d.manager_id
WHERE d.start_date IS NOT NULL AND d.end_date IS NULL
ORDER BY 6 DESC;"""}


class PimManager:

    """
    PimManager class for managing the projects and overall project information
    """

    def __init__(self, db_login, table_route=[]):
        self.db_client = DbManager(*db_login)
        self.tables = DbManager(*db_login).tables
        self.table_route = table_route
        self.active_table = self.table_route[0]

    #TODO  BRUG AF %s placeholders i SQL for at forhindre SQL injection

    # Refresher databasen - bruges efter commits, så du kan se ændringerne realtime.
    def refresh_db(self):
        self.db_client = DbManager(*db_login)
        self.tables = DbManager(*db_login).tables

    # returnere fra portfolio tabellen, alle eller med et id.
    def get_portfolios(self, portfolio_id=None):
        if portfolio_id:
            portfolio = self.db_client.run_query(f"SELECT * FROM portfolio WHERE id = {portfolio_id};")
        else:
            portfolio = self.db_client.run_query(f"SELECT * FROM portfolio;")

        return portfolio

    # Kan senere bruges til direkte visualisering i applikation, hvor projekt dato´er skal bruges
    """
    def get_projects_dates(self, project_id=None, lookup_id=None, lookup_table=None):
        if project_id:
            project = self.db_client.run_query(f"SELECT * FROM project WHERE id = {project_id};")
        elif lookup_id:
            project = self.db_client.run_query(f"SELECT * FROM project WHERE {lookup_table} = {lookup_id};")
        else:
            project = self.db_client.run_query(f"SELECT * FROM project;")
        return [p[3:6] for p in project]

    """

    # returnere fra project tabellen, alle, med project id eller med et angivet portfolio_id(lookup_tabel,lookup_id).
    def get_projects(self, project_id=None, lookup_id=None, lookup_table=None):

        if project_id:
            project = self.db_client.run_query(f"SELECT * FROM project WHERE id = {project_id};")
        elif lookup_id:
            print(f"SELECT * FROM project WHERE {lookup_table} = {lookup_id};")
            project = self.db_client.run_query(f"SELECT * FROM project WHERE {lookup_table} = {lookup_id};")
        else:
            project = self.db_client.run_query(f"SELECT * FROM project;")


        return project

    # returnere fra product tabellen, alle, med product id eller med et angivet project_id(lookup_tabel,lookup_id).
    def get_products(self, product_id=None, lookup_id=None, lookup_table=None):
        if product_id:
            product = self.db_client.run_query(f"SELECT * FROM product WHERE id = {product_id};")
        elif lookup_id:
            product = self.db_client.run_query(f"SELECT * FROM product  WHERE {lookup_table} = {lookup_id};")
        else:
            product = self.db_client.run_query(f"SELECT * FROM product;")
        return product

    # returnere fra design tabellen, alle eller med et id.
    def get_designs(self, product_id=None, lookup_id=None, lookup_table=None):
        if product_id:
            design = self.db_client.run_query(f"SELECT * FROM design WHERE product_id = {product_id};")
        elif lookup_id:
            design = self.db_client.run_query(f"SELECT * FROM design WHERE id = {lookup_id};")
        else:
            design = self.db_client.run_query(f"SELECT * FROM design;")
        return design

    # returnere fra construction tabellen, alle eller med et id.
    def get_constructions(self, product_id=None, lookup_id=None, lookup_table=None):
        if product_id:
            construction = self.db_client.run_query(f"SELECT * FROM construction WHERE product_id = {product_id};")
        elif lookup_id:
            construction = self.db_client.run_query(f"SELECT * FROM construction WHERE id = {lookup_id};")
        else:
            construction = self.db_client.run_query(f"SELECT * FROM construction;")
        return construction

    # returnere fra prototype tabellen, alle eller med et id.
    def get_prototypes(self, product_id=None, lookup_id=None, lookup_table=None):
        if product_id:
            prototype = self.db_client.run_query(f"SELECT * FROM prototype WHERE product_id = {product_id};")
        elif lookup_id:
            prototype = self.db_client.run_query(f"SELECT * FROM prototype WHERE id = {lookup_id};")

        else:
            prototype = self.db_client.run_query(f"SELECT * FROM prototype;")
        return prototype

    #Returnere data fra employees, alle eller med specifikt id.
    def get_employees(self, employee_id=None):
        if employee_id:
            employee = self.db_client.run_query(f"SELECT * FROM employee WHERE id = {employee_id};")
        else:
            employee = self.db_client.run_query(f"SELECT * FROM employee;")
        return employee

    #bruges som hjælpefunktion til at hente den aktive table i vores GUI.
    def get_active(self, active_table, id = None, lookup_id=None, lookup_table=None):
        if active_table == "portfolio":
            return self.get_portfolios(id)
        elif active_table == "project":
            return self.get_projects(id, lookup_id, lookup_table)
        elif active_table == "product":
            return self.get_products(id, lookup_id, lookup_table)
        elif active_table == "design":
            return self.get_designs(id, lookup_id, lookup_table)
        elif active_table == "construction":
            return self.get_constructions(id, lookup_id, lookup_table)
        elif active_table == "prototype":
            return self.get_prototypes(id, lookup_id, lookup_table)
        elif active_table == "employee":
            return self.get_employees(id) if id else self.get_employees()
        else:
            return None

    #Bruges til at lave opdateringer af databasen, hvor vi bruger update_query method fra DbManager.
    def update_database(self, table,field, value, id):
        #print(f"UPDATE {self.db_client.db_name}.{table} SET {field} = '{value}' WHERE id = {id};")
        self.db_client.update_query(f"UPDATE {self.db_client.db_name}.{table} SET {field} = '{value}' WHERE id = {id};")




