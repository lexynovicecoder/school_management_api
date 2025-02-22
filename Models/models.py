from sqlmodel import Field, SQLModel,Relationship
from datetime import datetime,timedelta


class Authority(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    full_name: str
    email: str
    hashed_password: str

class Student(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    full_name: str
    birth_date: datetime 
    
