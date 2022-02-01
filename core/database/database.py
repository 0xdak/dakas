from distutils.log import error
from mimetypes import init
from core.database.config import config
from pydantic import BaseModel

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from datetime import datetime


LOG_FILE = "dakas.log"

class DatabaseManager():
    session = None

    def __init__(self):
        if self.session is not None:
            return # TODO is it dangerous???
        params = config()

        try:
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
        except Exception as e:
            with open(LOG_FILE, 'a') as f:
                print(f'{datetime.now()} : {str(e)}', file=f)

    def add(self, any):
        print(f'{type(any)} is adding to DB')
        print(*list(any.__dict__.items()), sep="\n    ")
        self.session.add(any)
        self.session.commit()
        self.session.close()
    
        