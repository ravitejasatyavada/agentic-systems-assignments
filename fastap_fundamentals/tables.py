from sqlalchemy import Table, MetaData, Column, Integer, String
from fastap_fundamentals.db import engine

metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50), nullable=False),
    Column("email", String, unique=True, nullable=False)
)


def create_table():
    metadata.create_all(engine)
