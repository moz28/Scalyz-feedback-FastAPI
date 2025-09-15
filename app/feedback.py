from typing import List

from sqlalchemy import Column, DateTime, Index, Integer, String, Text
from sqlalchemy.orm import Session
from sqlalchemy.sql import func

from .db import Base
from .feedback_schema import FeedbackCreate


class Feedback(Base):
	"""Feedback entity."""

	__tablename__ = "feedbacks"
	__table_args__ = (
		Index("ix_feedbacks_created_at", "created_at"),
		{"comment": "Table for storing user feedback"},
	)

	id = Column(Integer, primary_key=True, index=True, autoincrement=True)
	name = Column(String(100), nullable=True, comment="User name (optional)")
	email = Column(String(255), nullable=True, comment="User email (optional)")
	message = Column(Text, nullable=False, comment="Feedback message (required)")
	created_at = Column(
		DateTime(timezone=True),
		server_default=func.now(),
		nullable=False,
		comment="Timestamp when feedback was created",
	)

	def __repr__(self):
		return f"<Feedback(id={self.id}, name='{self.name}', created_at='{self.created_at}')>"


def create_feedback(db: Session, feedback: FeedbackCreate) -> Feedback:
	"""Create feedback in database."""
	db_feedback = Feedback(name=feedback.name, email=feedback.email, message=feedback.message)
	db.add(db_feedback)
	db.commit()
	db.refresh(db_feedback)
	return db_feedback


def get_feedbacks(db: Session, skip: int = 0, limit: int = 100) -> List[Feedback]:
	"""List feedbacks ordered by most recent first."""
	return (
		db.query(Feedback)
		.order_by(Feedback.created_at.desc())
		.offset(skip)
		.limit(limit)
		.all()
	)


def get_feedback_by_id(db: Session, feedback_id: int) -> Feedback:
	"""Get feedback by id."""
	return db.query(Feedback).filter(Feedback.id == feedback_id).first()


def get_feedbacks_count(db: Session) -> int:
	"""Count feedbacks."""
	return db.query(Feedback).count()
