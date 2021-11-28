"""
    Defined models to be used with the Database of choice.
"""
# I am defining db in another module, which also import these models - could be a problem
from pony import orm
from .database import db 

class TempCheck(db.Entity):
    temp_value = Required(Decimal, precision=6, scale=2)
    time_of_measurement = Required(datetime)
    

