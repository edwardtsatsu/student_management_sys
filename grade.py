import uuid
from sqlalchemy import UUID, String, func, Column, ForeignKey, DateTime, Text, Double
from sqlalchemy.orm import relationship

from .base import Base


class Grade(Base):
    __tablename__ = 'grade'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    student_id = Column(UUID(as_uuid=True), ForeignKey('student.id'))
    grade_letter = Column(String)
    semester = Column(String)
    score = Column(String)
    created_at = Column(DateTime, server_default=func.now(), nullable=True)
    updated_at = Column(DateTime, server_onupdate=func.now(), nullable=True)

    student = relationship('Student', backref='grades')
