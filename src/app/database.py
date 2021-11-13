"""
    Module to create DB object, bind it and declare DB related functions.
"""
import os
from pony import orm 


def create_database(env:str, db):
    """ Create DB based on the env variable"""

    if env == 'DEV':
        db.bind(provider='sqlite', filename='database_dev.sqlite', create_db=True)
    elif env == 'TEST':
        db.bind(provider='sqlite', filename=':memory:')
    else:
        db.bind(provider='sqlite', filename='database_dev.sqlite', create_db=True)

    db.generate_mapping(create_tables=True)
    
