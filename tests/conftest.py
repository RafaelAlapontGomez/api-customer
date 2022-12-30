import logging
import os
from playhouse.sqlite_ext import SqliteDatabase

os.environ['RUN_ENV'] = 'test'

from app.v1.model import city_model, customer_model
from app.v1.utils.settings import Settings

logger = logging.getLogger(__name__)  # the __name__ resolve to "uicheckapp.services"
                                      # This will load the uicheckapp logger

settings: Settings = Settings()

test_db = SqliteDatabase(':memory:')
MODELS = [customer_model.Customer, city_model.City]

def pytest_sessionstart(session):
    test_db.connect()
    test_db.create_tables(MODELS)

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
    test_db.drop_tables(MODELS)
    test_db.close()




