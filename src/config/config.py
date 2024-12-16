import os
from dotenv import load_dotenv

load_dotenv()
class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    LLAMA_CLOUD_API_KEYS = [
        os.getenv(f"LLAMA_CLOUD_API_KEY_{i}") for i in range(1, 9) if os.getenv(f"LLAMA_CLOUD_API_KEY_{i}")
    ]
    
    @staticmethod
    def validate():
        if not Config.OPENAI_API_KEY:
            raise EnvironmentError("OPENAI_API_KEY is not set in environment variables.")
        if not Config.LLAMA_CLOUD_API_KEYS:
            raise EnvironmentError("No valid LLAMA_CLOUD_API_KEYS found in environment variables.")
