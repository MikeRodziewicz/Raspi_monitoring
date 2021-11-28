"""
 Module to handle database related function, including initialization of the DB, 
 binding and table creation. 

"""
# could be a problem with circular imports here. 
from pony import orm 
from .models import TempCheck

db = Database()


