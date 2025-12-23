import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings:
    PROJECT_NAME: str = "Spur AI Live Chat"

    # LLM Configuration
    GROQ_API_KEY: str | None = os.getenv("GROQ_API_KEY")
    LLM_MODEL: str = "llama-3.1-8b-instant"

    # LLM API URL
    GROQ_API_URL: str = "https://api.groq.com/openai/v1/chat/completions"

settings = Settings()
