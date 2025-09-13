from sqlalchemy import Column, Integer, String, Text, DateTime, Index
from sqlalchemy.sql import func
from .db import Base

class Feedback(Base):
    """
    Feedback model for storing user feedback data.
    
    Attributes:
        id: Primary key (auto-increment)
        name: Optional user name
        email: Optional user email
        message: Required feedback message
        created_at: Timestamp when feedback was created (auto-generated)
    """
    __tablename__ = "feedbacks"
    __table_args__ = (
        Index('ix_feedbacks_created_at', 'created_at'),
        {'comment': 'Table for storing user feedback'}
    )
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=True, comment="User name (optional)")
    email = Column(String(255), nullable=True, comment="User email (optional)")
    message = Column(Text, nullable=False, comment="Feedback message (required)")
    created_at = Column(
        DateTime(timezone=True), 
        server_default=func.now(), 
        nullable=False,
        comment="Timestamp when feedback was created"
    )
    
    def __repr__(self):
        return f"<Feedback(id={self.id}, name='{self.name}', created_at='{self.created_at}')>"