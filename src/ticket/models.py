import datetime

from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from pydantic import BaseModel


class Ticket(BaseModel):
    id: Column(Integer, primary_key=True, index=True)
    department_id = Column(Integer, ForeignKey("department.id"))
    user_id = Column(Integer, ForeignKey("user.id"))
    title: Column(String, index=True)
    message: Column(String, nullable=True)
    priority: Column(String)
    link: Column(String)
    state: Column(Integer, default=1)
    created_at: datetime.datetime
    updated_at: datetime.datetime | None = None
    deleted_at: datetime.datetime | None = None
