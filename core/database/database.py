from mimetypes import init
from core.database.config import config
from pydantic import BaseModel

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker





class DatabaseManager():
    session: sessionmaker

    def __init__(self):
        params = config()
        database_config = f'postgresql+psycopg2://' + \
            f'{params["user"]}:' + \
            f'{params["password"]}@' + \
            f'{params["host"]}:5433/' + \
            f'{params["database"]}'

        print("Creating Database Engine...")
        engine = create_engine(database_config)
        # create a configured "Session" class
        print("Binding Database Engine...")
        Session = sessionmaker(bind=engine)

        # create a Session
        print("Creating Database Session...")
        self.session = Session()
        print("Database is Ready")

    def add(self, any):
        self.session.add(any)
        self.session.commit()
        self.session.close()
        