from mimetypes import init
from core.database.config import config
from pydantic import BaseModel

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.models import User

params = config()
database_config = f'postgresql+psycopg2://\
    {params["user"]}:\
    {params["password"]}@\
    {params["host"]}:5433/\
    {params["database"]}'


class DatabaseManager():
    session: sessionmaker

    def __init__(self):
        print("Creating Database Engine...")
        engine = create_engine(database_config)
        # create a configured "Session" class
        print("Binding Database Engine...")
        Session = sessionmaker(bind=engine)


        # create a Session
        print("Creating Database Session...")
        self.session = Session()
        

    def add(self, any):
        print(f"Adding {type(any)} to database...")


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
