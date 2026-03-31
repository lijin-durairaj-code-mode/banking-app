from sqlalchemy import create_engine, MetaData, Table, text
from sqlalchemy.orm import sessionmaker, declarative_base
from models.employees import employee

DB_URL = "postgresql://postgres:1q2w3e4LD14!@localhost:5432/dummy"

engine = create_engine(DB_URL)
metadata = MetaData()
employees = Table("employees", metadata, autoload_with=engine)


def get_employee_details(_query_text):
    query = text(_query_text)
    result_row = []
    with engine.connect() as conn:
        result = conn.execute(query)
        for row in result:
            result_row.append(row)
    return result_row
