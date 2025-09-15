# Feedback API

A robust FastAPI microservice for collecting and retrieving user feedback, with PostgreSQL persistence, Alembic migrations, and full Docker containerization.  

---

## Features
- RESTful API with **FastAPI**  
- PostgreSQL database using **SQLAlchemy 2.x**  
- Database migrations with **Alembic**  
- **Dockerfile** & **Docker Compose** for local and production  
- **Pydantic v2** for validation  
- Health check endpoint for monitoring  

---

## API Endpoints
- `GET /healthz` → service health status  
- `POST /feedbacks` → create new feedback  
- `GET /feedbacks` → list feedbacks (with pagination)  

---

## Quick Start

### Prerequisites
- Docker & Docker Compose  
- Python 3.12+ (for local dev)  

### 1. Clone & setup
```bash
git clone <your-repo>
cd feedback-api
cp .env.example .env
2. Run with Docker Compose (recommended)
bash
Copier le code
# Start API + DB
docker-compose up --build

# Or in background
docker-compose up -d --build
The API will be available at http://localhost:8000.
Migrations are applied automatically on container start.

3. Local development
bash
Copier le code
# Start PostgreSQL
docker run --name postgres-dev -e POSTGRES_USER=feedback_user \
  -e POSTGRES_PASSWORD=feedback_password \
  -e POSTGRES_DB=feedback_db \
  -p 5432:5432 -d postgres:16-alpine

# Install deps
pip install -r requirements.txt

# Run migrations
alembic upgrade head

# Start API
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
Database Migrations
This project uses Alembic.
Common commands:

bash
Copier le code
# Apply migrations
alembic upgrade head

# Rollback last migration
alembic downgrade -1

# Show current revision
alembic current

# Create new migration from models
alembic revision --autogenerate -m "Add column"

# Create empty migration
alembic revision -m "Custom migration"
Docker Commands
bash
Copier le code
# Build & start
docker-compose up --build

# Stop
docker-compose down

# Logs
docker-compose logs -f api
docker-compose logs -f db

# Exec into container
docker-compose exec api bash
docker-compose exec db psql -U feedback_user -d feedback_db
markdown
Copier le code

👉 Étapes pour mettre à jour :  
1. Ouvre ton projet dans VS Code (ou ton éditeur).  
2. Remplace le contenu de `README.md` par ce texte.  
3. Commit & push :  
   ```bash
   git add README.md
   git commit -m "docs: improve README with clean instructions"
   git push
