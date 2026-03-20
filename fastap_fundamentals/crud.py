from fastap_fundamentals.db import engine
from fastap_fundamentals.tables import users
from sqlalchemy import insert, select, update, delete


def create_user(input_name: str, email_string: str):
    with engine.connect() as conn:
        query = insert(users).values(name=input_name, email=email_string)
        conn.execute(query)
        conn.commit()


def get_user_by_id(input_user_id: int):
    with engine.connect() as conn:
        query = select(users).where(users.c.id == input_user_id)
        data = conn.execute(query).first()
        return data


def get_all_users():
    with engine.connect() as conn:
        query = select(users)
        data = conn.execute(query).fetchall()
        return data


def update_user_name(input_user_id:int , input_user_name: str):
    with engine.connect() as conn:
        query = update(users).where(users.c.id == input_user_id).values(name = input_user_name)
        conn.execute(query)
        conn.commit()


def delete_user_by_id(input_user_id: int):
    with engine.connect() as conn:
        query = delete(users).where(users.c.id == input_user_id)
        conn.execute(query)
        conn.commit()
