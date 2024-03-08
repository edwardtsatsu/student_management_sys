import uuid
from sqlalchemy import UUID, Numeric, String, func, Column, ForeignKey, DateTime, Text, Double
from sqlalchemy.orm import relationship

from .base import Base


class PaymentRequest(Base):
    __tablename__ = 'payment_request'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    amount = Column(Numeric)
    student_id = Column(UUID(as_uuid=True), ForeignKey('student.id'))
    created_at = Column(DateTime, server_default=func.now(), nullable=True)
    updated_at = Column(DateTime, server_onupdate=func.now(), nullable=True)

    student = relationship('Student', backref='payment_requests')