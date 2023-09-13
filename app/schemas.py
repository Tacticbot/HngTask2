from pydantic import BaseModel

class PersonBase(BaseModel):
    name: str

class PersonCreate(PersonBase):
    pass

class Person(PersonBase):
    user_id: int

    class Config:
        orm_mode = True