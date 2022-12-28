from fastapi import HTTPException, status

from app.v1.model.customer_model import Customer as CustomerModel
from app.v1.model.city_model import City as CityModel

from app.v1.schema import customer_schema
from app.v1.schema.city_schema import CityBase

def create_customer(customer: customer_schema.CustomerRegister):
    get_customer = CustomerModel.filter(CustomerModel.email == customer.email   ).first()
    if get_customer:
        msg = "customer already registered"
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=msg)
    
    db_customer = mappingDtoToEntity(customer)

    db_customer.save()

    return mappingEntityToDto(db_customer)

def get_all_customers():
    get_customers = CustomerModel.select()

    list_customers = []
    for customer in get_customers:
        list_customers.append(mappingEntityToDto(customer))

    return list_customers

def get_customer(customer_id: int):
    customer = CustomerModel.filter(CustomerModel.id == customer_id).first()

    if not customer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Customer not found"
        )

    return mappingEntityToDto(customer)

def update_customer(customer_id: int, customer: customer_schema.CustomerRegister):
    db_customer: CustomerModel = CustomerModel.filter(CustomerModel.id == customer_id).first()

    if not db_customer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Customer not found"
        )

    db_city = CityModel.filter(CityModel.code == customer.city)

    if not db_city:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="City not found"
        )

    print ("db_customer ==> " + str(db_customer.id))

    db_customer.firstName = customer.firstName
    db_customer.lastName = customer.lastName
    db_customer.birthdate = customer.birthdate
    db_customer.email = customer.email
    db_customer.active = customer.active
    db_customer.phone = customer.phone
    db_customer.city = db_city

    db_customer.save()

    return mappingEntityToDto(db_customer)

def delete_customer(customer_id: int):
    db_customer: CustomerModel = CustomerModel.filter(CustomerModel.id == customer_id).first()

    if not db_customer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Customer not found"
        )

    db_customer.delete_instance()

def mappingEntityToDto(customer: CustomerModel):
    return customer_schema.Customer(
        id = customer.id,
        firstName = customer.firstName,
        lastName = customer.lastName,
        email = customer.email,
        birthdate = customer.birthdate,
        active = customer.active,
        phone = customer.phone,
        city = CityBase(
            code = customer.city.code, 
            description= customer.city.description
        )     
    )

def mappingDtoToEntity(customer: customer_schema.CustomerRegister):
    return CustomerModel(
        firstName = customer.firstName,
        lastName = customer.lastName,
        email = customer.email,
        birthdate = customer.birthdate,
        active = customer.active,
        phone = customer.phone,
        city = customer.city
    )    



