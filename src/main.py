
import os 
from pony import orm
from dotenv import load_dotenv 
from app.database import create_database  

load_dotenv()
env = os.getenv('ENV', 'DEV')

db = orm.Database()
create_database(env, db)
print(db)
