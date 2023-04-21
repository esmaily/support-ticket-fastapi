import datetime

from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from pydantic import BaseModel


class Department(BaseModel):
    id: Column(Integer, primary_key=True, index=True)
    title: Column(String, index=True)
    slug: Column(String)
    created_at: datetime.datetime
    updated_at: datetime.datetime | None = None
    deleted_at: datetime.datetime | None = None
