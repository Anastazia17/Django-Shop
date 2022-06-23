from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

PATH_DB = 'db.sqlite3'


class Repository:
    def __init__(self, path_db):
        self.engine = create_engine(f'sqlite:///{path_db}?check_same_thread=False')
        self.create_base()
        self.session = self.get_session()

    def create_base(self):
        base = declarative_base()
        base.metadata.create_all(self.engine)

    def get_session(self):
        session = sessionmaker(bind=self.engine)
        session = session()
        return session


if __name__ == '__main__':
    REP = Repository(PATH_DB)
