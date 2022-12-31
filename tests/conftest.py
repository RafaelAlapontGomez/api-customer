import logging
import os
import pymysql

os.environ['RUN_ENV'] = 'test'

from app.v1.model import city_model, customer_model
from app.v1.utils.settings import Settings

logger = logging.getLogger(__name__)  # the __name__ resolve to "uicheckapp.services"
                                      # This will load the uicheckapp logger

settings: Settings = Settings()

MODELS = [customer_model.Customer, city_model.City]

def mysql_connection():
    con = pymysql.connect(
        host=settings.db_host, 
        port=settings.db_port, 
        user=settings.db_user,
        passwd=settings.db_pass
    )
    return con

def delete_database():

    if not settings.db_name.startswith("test_"):
        raise Exception(f'Invalid name for database = {settings.db_name}')

    sql_drop_db = f"DROP DATABASE IF EXISTS {settings.db_name}"
    logger.info(f"DROP DATABASE IF EXISTS {settings.db_name}")

    con = mysql_connection()
    cursor = con.cursor()
    cursor.execute(sql_drop_db)
    con.close()

def create_database():
    sql_create_db = f"CREATE DATABASE {settings.db_name};"
    sql_use_db = f"USE {settings.db_name};"

    con = mysql_connection()
    cursor = con.cursor()
    cursor.execute(sql_create_db)
    cursor.execute(sql_use_db)
    con.close()

def pytest_sessionstart(session):

    delete_database()
    create_database()

    from app.v1.utils.db import db

    with db:
        db.create_tables(MODELS)

    create_cities()

def create_cities():
    data_source = [
        {'code': 'MAD', 'description': 'Madrid'},
        {'code': 'BAR', 'description': 'Barcelona'},
        {'code': 'BIL', 'description': 'Bilbao'}
    ]

    city_model.City.insert_many(data_source).execute()

def pytest_sessionfinish(session, exitstatus):
    logger.info('sessions finish')
    delete_database()



