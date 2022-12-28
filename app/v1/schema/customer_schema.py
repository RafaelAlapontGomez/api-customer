from typing import Union

from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr
from pydantic.datetime_parse import parse_date, get_numeric

from app.v1.schema.city_schema import CityBase

class CustomerBase(BaseModel):

    firstName: str = Field(
        ...,
        example="nombre"
    )
    lastName: str = Field(
        ...,
        example="apellido1 apellido2"
    )
    birthdate: str = Field(
        ...,
        example="19/07/1963"
    )
    email: EmailStr = Field(
        ...,
        example="myemail@cosasdedevs.com"
    )
    active: bool = Field(
        default=True,
        example=True
    )
    phone: Union[str, None] = Field(
        default=None,
        example="610524674"
    )

class Customer(CustomerBase):
    id: int = Field(
        ...,
        example="5"
    )
    city: CityBase = Field(
        ...
    )

class CustomerRegister(CustomerBase):
    city: str = Field(
        example="MAD"
    )
