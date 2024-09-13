from sqlalchemy import Column, Integer, String
import pandas as pd

from . import engine, Base

class Source(Base):
    __tablename__ = 'source'
    id = Column(Integer, primary_key=True, autoincrement="auto")
    name = Column(String)
    flag = Column(String)

class Target(Base):
    __tablename__ = 'target'
    id = Column(Integer, primary_key=True, autoincrement="auto")
    name = Column(String)
    flag = Column(String)

# Create tables in the database
Base.metadata.create_all(engine)

def insert_csv_to_db(csv_file, table_class, engine):
    df = pd.read_csv(csv_file)

    with engine.connect() as connection:
        df.to_sql("source", connection, if_exists='replace', index=False)
        df.to_sql("target", connection, if_exists='replace', index=False)

def main():
    insert_csv_to_db('db_config/Dummy.csv', 'source', engine)
    insert_csv_to_db('db_config/Dummy.csv', 'target', engine)

if __name__ == "__main__":
    main()
