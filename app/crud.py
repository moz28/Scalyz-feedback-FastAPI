from sqlalchemy.orm import Session
from typing import List

from .models import Feedback
from .schemas import FeedbackCreate

def create_feedback(db: Session, feedback: FeedbackCreate) -> Feedback:
    """
    Create a new feedback entry in the database.
    
    Args:
        db: Database session
        feedback: Feedback data to create
        
    Returns:
        Created feedback object with id and created_at
    """
    db_feedback = Feedback(
        name=feedback.name,
        email=feedback.email,
        message=feedback.message
    )
    db.add(db_feedback)
    db.commit()
    db.refresh(db_feedback)
    return db_feedback

def get_feedbacks(db: Session, skip: int = 0, limit: int = 100) -> List[Feedback]:
    """
    Retrieve feedbacks from the database, ordered by most recent first.
    
    Args:
        db: Database session
        skip: Number of records to skip (for pagination)
        limit: Maximum number of records to return
        
    Returns:
        List of feedback objects
    """
    return (
        db.query(Feedback)
        .order_by(Feedback.created_at.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )

def get_feedback_by_id(db: Session, feedback_id: int) -> Feedback:
    """
    Get a specific feedback by ID.
    
    Args:
        db: Database session
        feedback_id: ID of the feedback to retrieve
        
    Returns:
        Feedback object or None if not found
    """
    return db.query(Feedback).filter(Feedback.id == feedback_id).first()

def get_feedbacks_count(db: Session) -> int:
    """
    Get total count of feedbacks in the database.
    
    Args:
        db: Database session
        
    Returns:
        Total number of feedback entries
    """
    return db.query(Feedback).count()