from app.v1.model.customer_model import Customer

from app.v1.utils.db import db

def create_tables():
    with db:
        db.create_tables([Customer])
