from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URL: str
    JWT_SECRET_KEY : str = 'test'

    class Config:
        env_file = "../.env"

settings = Settings()