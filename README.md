Feedback API
A robust FastAPI microservice for collecting and retrieving user feedback, with PostgreSQL persistence, Alembic migrations, and full Docker containerization support.
🚀 Features

RESTful API with FastAPI
PostgreSQL database with SQLAlchemy 2.x
Alembic for database migrations and versioning
Full Docker support (development and production)
Pydantic v2 for data validation
Health checks for monitoring
Production-ready configuration

📋 API Endpoints
Health Check

GET /healthz - Service health status

Feedback Operations

POST /feedbacks - Create new feedback
GET /feedbacks - List feedbacks (with pagination)

🛠️ Quick Start
Prerequisites

Docker and Docker Compose
Python 3.12+ (for local development)

1. Clone and Setup
bashgit clone <your-repo>
cd feedback-api

# Copy environment file
cp .env.example .env
2. Run with Docker Compose (Recommended)
bash# Start all services (API + Database)
docker-compose up --build

# Run in background
docker-compose up -d --build
The API will be available at http://localhost:8000
Note: Migrations are automatically applied when the API container starts.
3. Local Development Setup
bash# Start PostgreSQL with Docker
docker run --name postgres-dev -e POSTGRES_USER=feedback_user \
  -e POSTGRES_PASSWORD=feedback_password \
  -e POSTGRES_DB=feedback_db \
  -p 5432:5432 -d postgres:16-alpine

# Install dependencies
pip install -r requirements.txt

# Run initial migration
alembic upgrade head

# Run the API
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
🗄️ Database Migrations
This project uses Alembic for database migrations and schema versioning.
Migration Commands
bash# Apply all pending migrations
alembic upgrade head

# Downgrade by one migration
alembic downgrade -1

# Show current migration
alembic current

# Show migration history
alembic history

# Create new migration (auto-generate from model changes)
alembic revision --autogenerate -m "Add new column"

# Create empty migration (for manual changes)
alembic revision -m "Custom migration"
Using the Migration Script
A convenient script is provided for migration management:
bash# Apply migrations
python scripts/migrate.py upgrade

# Create new migration
python scripts/migrate.py create "Add user_id to feedbacks"

# Show migration history
python scripts/migrate.py history

# Show current revision
python scripts/migrate.py current

## Feedback API

A robust FastAPI microservice for collecting and retrieving user feedback, with PostgreSQL persistence and full Docker containerization support.

## 🚀 Features

- **RESTful API** with FastAPI
- **PostgreSQL** database with SQLAlchemy 2.x
- **Full Docker support** (development and production)
- **Pydantic v2** for data validation
- **Health checks** for monitoring
- **Production-ready** configuration

## 📋 API Endpoints

### Health Check
- `GET /healthz` - Service health status

### Feedback Operations
- `POST /feedbacks` - Create new feedback
- `GET /feedbacks` - List feedbacks (with pagination)

## 🛠️ Quick Start

### Prerequisites
- Docker and Docker Compose
- Python 3.12+ (for local development)

### 1. Clone and Setup
```bash
git clone <your-repo>
cd feedback-api

# Copy environment file
cp .env.example .env
2. Run with Docker Compose (Recommended)
bash# Start all services (API + Database)
docker-compose up --build

# Run in background
docker-compose up -d --build
The API will be available at http://localhost:8000
3. Local Development Setup
bash# Start PostgreSQL with Docker
docker run --name postgres-dev -e POSTGRES_USER=feedback_user \
  -e POSTGRES_PASSWORD=feedback_password \
  -e POSTGRES_DB=feedback_db \
  -p 5432:5432 -d postgres:16-alpine

# Install dependencies
pip install -r requirements.txt

# Run the API
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

🐳 Docker Commands
# Build and start services
docker-compose up --build

# Stop services
docker-compose down

# View logs
docker-compose logs -f api
docker-compose logs -f db

# Execute commands in running containers
docker-compose exec api bash
docker-compose exec db psql -U feedback_user -d feedback_db