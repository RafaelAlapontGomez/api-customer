from datetime import datetime

from fastapi import HTTPException, status

from app.v1.model.customer_model import Customer as CustomerModel
from app.v1.schema import customer_schema
from app.v1.schema.city_schema import CityBase

def create_customer(customer: customer_schema.CustomerRegister):
    get_customer = CustomerModel.filter(CustomerModel.email == customer.email   ).first()
    if get_customer:
        msg = "customer already registered"
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=msg)
    
    db_customer = CustomerModel(
        firstName = customer.firstName,
        lastName = customer.lastName,
        email = customer.email,
        birthdate = customer.birthdate,
        active = customer.active,
        phone = customer.phone,
        city = customer.city
    )

    db_customer.save()

    response = customer_schema.Customer(
        id = db_customer.id,
        firstName = db_customer.firstName,
        lastName = db_customer.lastName,
        email = db_customer.email,
        birthdate = db_customer.birthdate,
        active = db_customer.active,
        phone = db_customer.phone,
        city = CityBase(code = db_customer.city.code, description= db_customer.city.description)        
    )

    return response




