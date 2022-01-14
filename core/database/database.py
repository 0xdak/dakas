from mimetypes import init
from config import config
from pydantic import BaseModel

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.models import User

params = config()
print(params["host"])



class DatabaseManager():
    session: sessionmaker

    def __init__(self):
        engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')
        # create a configured "Session" class
        Session = sessionmaker(bind=engine)

        # create a Session
        self.session = Session()

    def add(self, any):
        self.session.add(any)


    def deneme():
        """ Connect to the PostgreSQL database server """
        conn = None
        try:
            # read connection parameters
            params = config()

            print('Connecting to the PostgreSQL database...')
            conn = psycopg2.connect(**params)
            cur = conn.cursor()

            print('PostgreSQL database version:')
            cur.execute('SELECT version()')

            db_version = cur.fetchone()
            print(db_version)
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                print('Database connection closed.')

# connect()
# conn = psycopg2.connect("dbname=postgres user=postgres password=postgres")
