"""
 Module to handle database related function, including initialization of the DB, 
 binding and table creation. 

"""
from pony.orm import Database, Required
from datetime import datetime

db = Database()


class TempCheck(db.Entity):
    temp_value = Required(float)
    time_of_measurement = Required(datetime)


db.bind(provider='sqlite', filename='../db/database.sqlite', create_db=True)
db.generate_mapping(create_tables=True)
