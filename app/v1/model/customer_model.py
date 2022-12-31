import peewee
from peewee import ForeignKeyField

from app.v1.utils.db import db
from app.v1.model.city_model import City

class Customer(peewee.Model):
    id = peewee.AutoField(primary_key=True)
    firstName = peewee.CharField(max_length=20)
    lastName = peewee.CharField(max_length=40)
    birthdate = peewee.DateField(formats=['%Y-%m-%d'])
    email = peewee.CharField(unique=True, max_length=150)
    active = peewee.BooleanField(default=True)
    phone = peewee.CharField(max_length=9, null = True)
    city = ForeignKeyField(City, backref='cities')

    class Meta:
        database = db
