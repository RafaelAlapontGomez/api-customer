from app.v1.model.customer_model import Customer
from app.v1.model.city_model import City

from app.v1.utils.db import db

def create_tables():
    with db:
        db.create_tables([Customer, City])
        create_cities()

def create_cities():
    data_source = [
        {'code': 'MAD', 'description': 'Madrid'},
        {'code': 'BAR', 'description': 'Barcelona'},
        {'code': 'BIL', 'description': 'Bilbao'}
    ]

    City.insert_many(data_source).execute()