from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    """Application configuration using Pydantic Settings"""
    
    # Database configuration
    postgres_user: str = "feedback_user"
    postgres_password: str = "feedback_password"
    postgres_db: str = "feedback_db"
    postgres_host: str = "localhost"
    postgres_port: int = 5432
    
    # API configuration
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    
    @property
    def database_url(self) -> str:
        """Construct database URL from individual components"""
        return f"postgresql+psycopg://{self.postgres_user}:{self.postgres_password}@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False

# Create global settings instance
settings = Settings()