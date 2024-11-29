import os
from dotenv import load_dotenv
import psycopg2
""" Initialize DB """

load_dotenv()

def startup_db():
  """
  Initialize DB
  """
  dbname = os.getenv('DATABASE_NAME', 'aplication')
  dbuser = os.getenv('DATABASE_USERNAME', 'postgres')
  dbpass = os.getenv('DATABASE_PASSWORD', '')
  dbhost = os.getenv('DATABASE_HOST', 'localhost')
  dbport = os.getenv('DATABASE_PORT', '5432')
  
  print(dbpass)

  connection = psycopg2.connect(database=dbname, user=dbuser, password=dbpass, host=dbhost, port=dbport)
  connection.autocommit = True
  return connection