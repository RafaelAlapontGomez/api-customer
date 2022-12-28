import peewee

from app.v1.utils.db import db

class City(peewee.Model):
    code: str = peewee.CharField(primary_key=True, max_length=3)
    description: str = peewee.CharField(max_length=20)

    class Meta:
        database = db
