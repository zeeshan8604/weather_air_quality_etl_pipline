import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configuration for the Visual Crossing API
class Config:
    API_KEY = os.getenv("VISUALCROSSING_API_KEY")
    DATABASE_URL = os.getenv("DATABASE_URL")

    # Example default values; adjust or extend as needed
    DEFAULT_LOCATION = "ioannina"
    DEFAULT_START_DATE = "2023-09-04"
    DEFAULT_END_DATE = "2023-09-01"
