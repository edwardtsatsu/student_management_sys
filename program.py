import datetime
import uuid
from sqlalchemy import Boolean, String, func, Column, ForeignKey, DateTime, Text, Double
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID


from .base import Base


class Program(Base):
    __tablename__ = 'program'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String)
    alias = Column(String)
    duration = Column(String)
    department_id = Column(UUID(as_uuid=True), ForeignKey('department.id'))
    active_status = Column(Boolean)
    del_status = Column(Boolean)
    created_at = Column(DateTime, server_default=func.now(), nullable=True)
    updated_at = Column(DateTime, server_onupdate=func.now(), nullable=True)

    department = relationship('Department', backref='programs')