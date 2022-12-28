from fastapi import APIRouter
#from fastapi import Depends
from fastapi import status
from fastapi import Body

from app.v1.schema import customer_schema
from app.v1.service import customer_service

#from app.v1.utils.db import get_db

router = APIRouter(prefix="/api/v1")

@router.post(
    "/customer/",
    tags=["customers"],
    status_code=status.HTTP_201_CREATED,
    response_model=customer_schema.Customer,
    dependencies=[],
    summary="Create a new customer"
)
def create_customer(customer: customer_schema.CustomerRegister = Body(...)):
    return customer_service.create_customer(customer)

