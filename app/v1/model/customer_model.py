import peewee

from app.v1.utils.db import db

class Customer(peewee.Model):
    id = peewee.AutoField()
    firstName = peewee.CharField()
    lastField = peewee.CharField()
    birth = peewee.DateField()
    email = peewee.CharField()

    class Meta:
        database = db
