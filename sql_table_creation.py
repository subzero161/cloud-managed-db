## Correct way example here:  https://pypi.org/project/python-dotenv/ 
# use dotenv to load in environment variables
sudo apt-get install python3-dev default-libmysqlclient-dev 
pip install pymysql sqlalchemy

from sqlalchemy import create_engine
import sqlalchemy
from dotenv import load_dotenv
import os
load_dotenv()
MYSQL_HOSTNAME = os.getenv("MYSQL_HOSTNAME")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")


########

connection_string = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}:3306/{MYSQL_DATABASE}'
connection_string

engine = create_engine(connection_string)

#TABLENAME = MYSQL_USER + 'fakeTableAssignment1'

#fakeDataset.to_sql(TABLENAME, con=engine)