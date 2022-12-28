from pydantic import BaseModel
from pydantic import Field

class CityBase(BaseModel):
    code: str = Field(
        ...,
        example="MAD"
    ),
    description: str = Field(
        ...,
        example="Madrid"
    )

