from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///./students.db"


def create_db_connection():
    engine = create_engine(DATABASE_URL, echo=True)
    return engine
