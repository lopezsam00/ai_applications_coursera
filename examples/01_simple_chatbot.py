"""
Example 1: Simple Chatbot using OpenAI API

This example demonstrates:
- Setting up OpenAI client
- Creating a simple chat completion
- Handling basic conversation
"""

import sys
from pathlib import Path

# Add project root to path for imports
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from openai import OpenAI
from utils.config import config
from utils import get_openai_client, handle_api_error

def simple_chatbot():
    """Create a simple chatbot that responds to user input."""
    
    # Initialize OpenAI client with validation
    try:
        client = get_openai_client()
    except ValueError as e:
        print(f"❌ Configuration Error: {e}")
        print("\n📋 Setup Instructions:")
        print("1. Copy .env.template to .env")
        print("2. Add your OpenAI API key to the .env file")
        print("3. Run the script again")
        return
    
    print("Simple Chatbot (type 'quit' to exit)")
    print("-" * 50)
    
    # Conversation history
    messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]
    
    while True:
        # Get user input
        user_input = input("\nYou: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("Goodbye!")
            break
        
        if not user_input:
            continue
        
        # Add user message to history
        messages.append({"role": "user", "content": user_input})
        
        try:
            # Create chat completion
            response = client.chat.completions.create(
                model=config.DEFAULT_MODEL,
                messages=messages,
                temperature=config.TEMPERATURE,
                max_tokens=config.MAX_TOKENS
            )
            
            # Extract assistant's response
            assistant_message = response.choices[0].message.content
            
            # Add assistant response to history
            messages.append({"role": "assistant", "content": assistant_message})
            
            # Print response
            print(f"\nAssistant: {assistant_message}")
            
        except Exception as e:
            handle_api_error(e)
            break

if __name__ == "__main__":
    simple_chatbot()
