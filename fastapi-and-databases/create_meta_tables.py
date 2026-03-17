from sqlalchemy import MetaData, Table, Column, Integer, String, CheckConstraint
from .create_database import create_db_connection

meta_obj = MetaData()

students = Table("Students",
                 meta_obj,
                 Column("id", Integer, primary_key=True),
                 Column("name", String, nullable=False),
                 Column("age", Integer, CheckConstraint("age >= 18")),
                 Column("city", String, nullable=True)
                 )


def create_tables():
    meta_obj.create_all(create_db_connection())
