from pydantic import BaseModel


class PersonBase(BaseModel):
    name: str