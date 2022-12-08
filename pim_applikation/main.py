import db_sql # import our database module

"""
Main.py 

This is the main file for the project. It contains the main function.

program consist of:
pim.py - pim module for the program
db.py - database module for the program
gui.py - gui module for the program

"""



if __name__ == "__main__":
    
    db = db_sql.DbManager() # create an instance of the database manager
    print(db)
    print(db.return_dict())