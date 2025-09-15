import logging

from fastapi import FastAPI

from .feedback_handlers import router as feedback_router

logging.basicConfig(level=logging.INFO)

app = FastAPI(title="Feedback API", version="1.0.0")

app.include_router(feedback_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)