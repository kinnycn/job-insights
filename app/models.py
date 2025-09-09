
from typing import Optional
from datetime import date
from sqlmodel import SQLModel, Field

class Job(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    company: str
    city: str
    salary_min: int
    salary_max: int
    experience: str
    posted_at: date
    desc: str
