# below libraries needed to load postgres variables from the ".env" file
import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.') / '.env'  # <-- this means goto the myWork dir and search for .env file there

load_dotenv(dotenv_path = env_path)

#--------------------------------------------------------------------------------------------------------#

class Settings:
    PROJECT_TITLE : str = 'Jobboard'
    PROJECT_VERSION : str = '0.1.0'

    POSTGRES_USER : str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER : str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT : str = os.getenv("POSTGRES_PORT", 5432)
    POSTGRES_DB : str = os.getenv("POSTGRES_DB", "fastapi_course_db")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"



# now we will create object of Settings class
settings = Settings()