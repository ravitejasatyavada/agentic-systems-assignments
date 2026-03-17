from .create_database import create_db_connection
from .create_meta_tables import students
from sqlalchemy import insert, select, update, delete


def create_user(input_name: str, input_age: int, input_city: str):
    with create_db_connection().connect() as conn:
        query = insert(students).\
            values(name=input_name,
                   age=input_age,
                   city=input_city)
        conn.execute(query)
        conn.commit()


def fetch_all_users():
    with create_db_connection().connect() as conn:
        query = select(students)
        data = conn.execute(query).fetchall()
        return data


def update_city(input_name: str, update_to_city: str):
    with create_db_connection().connect() as conn:
        query = update(students).where(students.c.name == input_name).values(city=update_to_city)
        conn.execute(query)
        conn.commit()


def delete_by_age(input_age: int):
    with create_db_connection().connect() as conn:
        query = delete(students).where(students.c.age < input_age)
        conn.execute(query)
        conn.commit()
