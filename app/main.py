from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
import logging

from .config import settings
from .db import get_db
from .schemas import FeedbackCreate, FeedbackResponse
from . import crud

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title="Feedback API",
    description="A microservice for collecting and retrieving user feedbacks",
    version="1.0.0",
)

@app.get("/healthz")
async def healthcheck():
    """Health check endpoint"""
    return {"status": "ok"}

@app.post("/feedbacks", response_model=FeedbackResponse)
async def create_feedback(
    feedback: FeedbackCreate,
    db: Session = Depends(get_db)
):
    """
    Create a new feedback entry.
    
    Args:
        feedback: Feedback data (name, email optional; message required)
        db: Database session
        
    Returns:
        Created feedback with id and created_at timestamp
    """
    try:
        db_feedback = crud.create_feedback(db=db, feedback=feedback)
        logger.info(f"Created feedback with id: {db_feedback.id}")
        return db_feedback
    except Exception as e:
        logger.error(f"Error creating feedback: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/feedbacks", response_model=List[FeedbackResponse])
async def get_feedbacks(
    skip: int = Query(0, ge=0, description="Number of records to skip"),
    limit: int = Query(100, ge=1, le=1000, description="Maximum number of records to return"),
    db: Session = Depends(get_db)
):
    """
    Retrieve feedbacks list, ordered by most recent first.
    
    Args:
        skip: Number of records to skip (for pagination)
        limit: Maximum number of records to return (1-1000)
        db: Database session
        
    Returns:
        List of feedback entries
    """
    try:
        feedbacks = crud.get_feedbacks(db=db, skip=skip, limit=limit)
        logger.info(f"Retrieved {len(feedbacks)} feedbacks (skip={skip}, limit={limit})")
        return feedbacks
    except Exception as e:
        logger.error(f"Error retrieving feedbacks: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)