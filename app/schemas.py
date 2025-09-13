from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Optional
from datetime import datetime

class FeedbackBase(BaseModel):
    """Base feedback schema with common fields"""
    name: Optional[str] = Field(None, max_length=100, description="User name (optional)")
    email: Optional[EmailStr] = Field(None, description="User email (optional)")
    message: str = Field(..., min_length=1, max_length=2000, description="Feedback message (required)")
    
    @field_validator('message')
    @classmethod
    def validate_message(cls, v: str) -> str:
        """Ensure message is not empty or just whitespace"""
        if not v or not v.strip():
            raise ValueError('Message cannot be empty or just whitespace')
        return v.strip()
    
    @field_validator('name')
    @classmethod
    def validate_name(cls, v: Optional[str]) -> Optional[str]:
        """Clean up name field if provided"""
        if v is not None:
            v = v.strip()
            if not v:  # If empty after stripping, set to None
                return None
        return v

class FeedbackCreate(FeedbackBase):
    """Schema for creating a new feedback entry"""
    pass

class FeedbackResponse(FeedbackBase):
    """Schema for feedback response (includes database fields)"""
    id: int = Field(..., description="Unique feedback identifier")
    created_at: datetime = Field(..., description="Timestamp when feedback was created")
    
    class Config:
        from_attributes = True  # For Pydantic v2 compatibility with SQLAlchemy