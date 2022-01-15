from mimetypes import init
from core.database.config import config
from pydantic import BaseModel

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


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
        