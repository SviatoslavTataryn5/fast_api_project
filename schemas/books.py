from pydantic import BaseModel

class BookBase(BaseModel):
    isbn: str
    name: str

class BookCreate(BookBase):
    pass

class BookRead(BookBase):
    class Config:
        orm_mode = True
