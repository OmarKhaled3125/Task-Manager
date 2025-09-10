import os
from datetime import timedelta

class Config:
SECRET_KEY = os.getenv("SECRET_KEY", "dev")
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = os.getenv("SQLALCHEMY_ECHO", "false").lower() == "true"

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "dev-jwt")
JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=30)
JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=7)

PAGE_SIZE_DEFAULT = int(os.getenv("PAGE_SIZE_DEFAULT", 20))
PAGE_SIZE_MAX = int(os.getenv("PAGE_SIZE_MAX", 100))

class TestConfig(Config):
TESTING = True
SQLALCHEMY_DATABASE_URI = os.getenv("TEST_DATABASE_URL", "sqlite:///:memory:")
SQLALCHEMY_ECHO = False