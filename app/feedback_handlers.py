import logging
from typing import List

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from .db import get_db
from .feedback import create_feedback as create_feedback_db
from .feedback import get_feedbacks as get_feedbacks_db
from .feedback_schema import FeedbackCreate, FeedbackResponse


router = APIRouter()

logger = logging.getLogger(__name__)


@router.get("/healthz")
async def healthcheck():
	"""Health check."""
	return {"status": "ok"}


@router.post("/feedbacks", response_model=FeedbackResponse)
async def create_feedback(feedback: FeedbackCreate, db: Session = Depends(get_db)):
	"""Create feedback."""
	db_feedback = create_feedback_db(db=db, feedback=feedback)
	logger.info(f"created feedback id={db_feedback.id}")
	return db_feedback


@router.get("/feedbacks", response_model=List[FeedbackResponse])
async def get_feedbacks(
	skip: int = Query(0, ge=0, description="Number of records to skip"),
	limit: int = Query(100, ge=1, le=1000, description="Maximum number of records to return"),
	db: Session = Depends(get_db),
):
	"""List feedbacks (most recent first)."""
	feedbacks = get_feedbacks_db(db=db, skip=skip, limit=limit)
	logger.info(f"retrieved feedbacks count={len(feedbacks)} skip={skip} limit={limit}")
	return feedbacks
