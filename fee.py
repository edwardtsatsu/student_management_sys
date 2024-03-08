import uuid
from sqlalchemy import UUID, Numeric, String, func, Column, ForeignKey, DateTime, Text, Double
from sqlalchemy.orm import relationship

from .base import Base


class Fee(Base):
    __tablename__ = 'fee'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    program_id = Column(UUID(as_uuid=True), ForeignKey('program.id'))
    amount = Column(Numeric)
    created_at = Column(DateTime, server_default=func.now(), nullable=True)
    updated_at = Column(DateTime, server_onupdate=func.now(), nullable=True)

    program = relationship('Program', backref='fees')
