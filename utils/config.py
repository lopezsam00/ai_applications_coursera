"""
Configuration utilities for loading environment variables and API keys.
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Configuration class for managing API keys and settings."""
    
    # OpenAI Configuration
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')
    OPENAI_ORG_ID = os.getenv('OPENAI_ORG_ID', '')
    
    # Model Configuration
    DEFAULT_MODEL = os.getenv('DEFAULT_MODEL', 'gpt-3.5-turbo')
    TEMPERATURE = float(os.getenv('TEMPERATURE', '0.7'))
    MAX_TOKENS = int(os.getenv('MAX_TOKENS', '500'))
    
    # Application Configuration
    DEBUG = os.getenv('DEBUG', 'True').lower() == 'true'
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    
    @classmethod
    def validate(cls):
        """Validate that required configuration is present."""
        if not cls.OPENAI_API_KEY:
            raise ValueError(
                "OPENAI_API_KEY not found. Please set it in your .env file or environment variables."
            )
        return True

# Create a config instance
config = Config()
