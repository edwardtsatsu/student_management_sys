import datetime
import uuid
from sqlalchemy import Boolean, String, func, Column, ForeignKey, DateTime, Text, Double
from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy.orm import relationship

from .base import Base

class User(Base):
    __tablename__ = 'user'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    role_id = Column(UUID(as_uuid=True), ForeignKey('role.id'))
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    middle_name = Column(String)
    email = Column(String)
    phone_number = Column(String)
    active_status = Column(Boolean)
    del_status = Column(Boolean)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    
    role = relationship('Role', backref='users')