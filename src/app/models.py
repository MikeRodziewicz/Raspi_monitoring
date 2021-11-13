"""
    Defining models to be used. 
"""
from app.database import db

class Email(db.Entity):
    sys_id = Required(str)
    email_number = Required(str)
    subject = Required(str) 
    body =  Required(str)

# TODO check the datetime options for Pony/mysql
class Incident(db.Entity):
    sys_id = Required(str)
    inc_number = Required(str)
    created_date = 
    resolved_date = 

