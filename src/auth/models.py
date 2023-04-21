import datetime

from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from pydantic import BaseModel


class Role(BaseModel):
    id: Column(Integer, primary_key=True, index=True)
    title: Column(String, index=True)
    slug: Column(String)
    created_at: datetime.datetime
    updated_at: datetime.datetime | None = None
    deleted_at: datetime.datetime | None = None


class Permission(BaseModel):
    id: Column(Integer, primary_key=True, index=True)
    title: Column(String, index=True)
    slug: Column(String)
    created_at: datetime.datetime
    updated_at: datetime.datetime | None = None
    deleted_at: datetime.datetime | None = None


class User(BaseModel):
    id: Column(Integer, primary_key=True, index=True)
    full_name: Column(String, index=True)
    message: Column(String, unique=True, index=True, nullable=False)
    is_active: Column(Boolean(), default=True)
    roles = relationship("Role", back_populates="owner")
    # permission_id = Column(Integer, ForeignKey("user.id"))
    created_at: datetime.datetime
    updated_at: datetime.datetime | None = None
    deleted_at: datetime.datetime | None = None
