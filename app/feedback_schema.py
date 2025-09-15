from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, Field, field_validator


class FeedbackBase(BaseModel):
	"""Base feedback schema."""

	name: Optional[str] = Field(None, max_length=100, description="User name (optional)")
	email: Optional[EmailStr] = Field(None, description="User email (optional)")
	message: str = Field(..., min_length=1, max_length=2000, description="Feedback message (required)")

	@field_validator("message")
	@classmethod
	def validate_message(cls, v: str) -> str:
		if not v or not v.strip():
			raise ValueError("Message cannot be empty or just whitespace")
		return v.strip()

	@field_validator("name")
	@classmethod
	def validate_name(cls, v: Optional[str]) -> Optional[str]:
		if v is not None:
			v = v.strip()
			if not v:
				return None
		return v


class FeedbackCreate(FeedbackBase):
	"""Payload for create."""


class FeedbackResponse(FeedbackBase):
	"""Response schema."""

	id: int = Field(..., description="Unique feedback identifier")
	created_at: datetime = Field(..., description="Timestamp when feedback was created")

	class Config:
		from_attributes = True
