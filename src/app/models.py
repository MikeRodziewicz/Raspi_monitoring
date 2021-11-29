"""
 Module to handle database related function, including initialization of the DB, 
 binding and table creation. 

"""
from pony.orm import * 

db = Database()


class TempCheck(db.Entity):
    temp_value = Required(Decimal, precision=6, scale=2)
    time_of_measurement = Required(datetime)


db.bind(provider='sqlite', filename='database.sqlite', create_db=True)
db.generate_mapping(create_tables=True)
