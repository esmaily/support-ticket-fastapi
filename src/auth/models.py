import datetime

from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from pydantic import BaseModel


class Role(BaseModel):
    id: Column(Integer, primary_key=True, index=True)
    name: Column(String, index=True)
    created_at: datetime.datetime
    updated_at: datetime.datetime | None = None
    deleted_at: datetime.datetime | None = None


class User(BaseModel):
    id: Column(Integer, primary_key=True, index=True)
    full_name: Column(String, index=True)
    email: Column(String, unique=True, index=True, nullable=False)
    password: Column(String, nullable=False)
    is_active: Column(Boolean(), default=True)
    roles = relationship("Role", back_populates="owner")
    # permission_id = Column(Integer, ForeignKey("user.id"))
    created_at: datetime.datetime
    updated_at: datetime.datetime | None = None
    deleted_at: datetime.datetime | None = None
