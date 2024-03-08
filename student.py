
import uuid
from sqlalchemy import UUID, Boolean, String, func, Column, ForeignKey, DateTime, Text, Double
from sqlalchemy.orm import relationship

from .base import Base

class Student(Base):
    __tablename__ = 'student'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey('user.id'))
    student_code = Column(String)
    completed_at = Column(DateTime)
    gender = Column(String)
    date_of_birth = Column(String)
    program_id = Column(UUID(as_uuid=True), ForeignKey('program.id'))
    active_status = Column(Boolean)
    del_status = Column(Boolean)
    created_at = Column(DateTime, server_default=func.now(), nullable=True)
    updated_at = Column(DateTime, server_onupdate=func.now(), nullable=True)

    user = relationship('User', backref='students')
    program = relationship('Program', backref='students')