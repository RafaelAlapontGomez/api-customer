import peewee
from peewee import ForeignKeyField

from app.v1.utils.db import db
from app.v1.model.city_model import City

class Customer(peewee.Model):
    id: int = peewee.AutoField(primary_key=True)
    firstName: str = peewee.CharField(max_length=20)
    lastName: str = peewee.CharField(max_length=40)
    birth = peewee.DateField()
    email: str = peewee.CharField(max_length=150)
    city = ForeignKeyField(City, backref='cities')

    class Meta:
        database = db
