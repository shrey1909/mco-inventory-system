# Configuration settings for the application
# Holds environment variables and constants

import os
import warnings
from dotenv import load_dotenv

load_dotenv()

_DEFAULT_SECRET = "change-this-secret-in-production"


class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    APP_NAME: str = "MCO Inventory System"
    DEBUG: bool = os.getenv("DEBUG", "true").lower() == "true"
    SECRET_KEY: str = os.getenv("SECRET_KEY", _DEFAULT_SECRET)
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))

    def __init__(self):
        if self.SECRET_KEY == _DEFAULT_SECRET:
            warnings.warn(
                "SECRET_KEY is using the default insecure value. "
                "Set the SECRET_KEY environment variable before deploying to production.",
                stacklevel=2,
            )


settings = Settings()