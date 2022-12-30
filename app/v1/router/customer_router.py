from typing import List

from fastapi import APIRouter
from fastapi import status
from fastapi import Body

from app.v1.schema import customer_schema
from app.v1.service import customer_service

router = APIRouter(prefix="/api/v1/customer", tags=["customers"])

@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=customer_schema.Customer,
    dependencies=[],
    summary="Create a new customer"
)
def create_customer(customer: customer_schema.CustomerRegister = Body(...)):
    return customer_service.create_customer(customer)

@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=List[customer_schema.Customer],
    dependencies=[],
    summary="Get all customer"
)
def get_all_customers():
    return customer_service.get_all_customers()

@router.get(
    "/{customer_id}",
    status_code=status.HTTP_200_OK,
    response_model=customer_schema.Customer,
    dependencies=[],
    summary="Get customer by id"
)
def get_customer(customer_id):
    return customer_service.get_customer(customer_id)    

@router.put(
    "/{customer_id}",
    status_code=status.HTTP_200_OK,
    response_model=customer_schema.Customer,
    dependencies=[],
    summary="Modify a customer"
)
def update_customer(customer_id, customer: customer_schema.CustomerRegister = Body(...)):
    return customer_service.update_customer(customer_id, customer)


@router.delete(
    "/{customer_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    dependencies=[]
)
def delete_customer(customer_id: int):
    customer_service.delete_customer(customer_id)

    return {
        'msg': 'Customer has been deleted successfully'
    }
