import uuid
from sqlalchemy import UUID, String, func, Column, ForeignKey, DateTime, Text, Double
from sqlalchemy.orm import relationship

from .base import Base


class Department(Base):
    __tablename__ = 'department'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String)
    created_at = Column(DateTime, server_default=func.now(), nullable=True)
    updated_at = Column(DateTime, server_onupdate=func.now(), nullable=True)