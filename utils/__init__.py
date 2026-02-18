"""
Utility functions for the AI applications.
"""

from openai import OpenAI
from .config import config


def get_openai_client():
    """
    Get a configured OpenAI client with validation.

    Returns:
        OpenAI: Configured OpenAI client

    Raises:
        ValueError: If API key is not configured
    """
    config.validate()
    return OpenAI(api_key=config.OPENAI_API_KEY)


def handle_api_error(error):
    """
    Provide helpful error messages for common API errors.

    Args:
        error: The exception that occurred
    """
    error_msg = str(error)

    if "api_key" in error_msg.lower():
        print("\n❌ API Key Error")
        print(
            "Please check that your OpenAI API key is correctly set in the .env file."
        )
    elif "rate_limit" in error_msg.lower():
        print("\n❌ Rate Limit Error")
        print("You've exceeded the API rate limit. Please wait a moment and try again.")
    elif "quota" in error_msg.lower():
        print("\n❌ Quota Exceeded")
        print("You've exceeded your API quota. Check your OpenAI account billing.")
    else:
        print(f"\n❌ Error: {error}")
        print("Please check your internet connection and API configuration.")
