"""
Example 1: Simple Chatbot using OpenAI API

This example demonstrates:
- Setting up OpenAI client
- Creating a simple chat completion
- Handling basic conversation
"""

from openai import OpenAI
from utils.config import config

def simple_chatbot():
    """Create a simple chatbot that responds to user input."""
    
    # Validate configuration
    try:
        config.validate()
    except ValueError as e:
        print(f"Configuration Error: {e}")
        print("\nPlease follow these steps:")
        print("1. Copy .env.template to .env")
        print("2. Add your OpenAI API key to the .env file")
        return
    
    # Initialize OpenAI client
    client = OpenAI(api_key=config.OPENAI_API_KEY)
    
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
            print(f"\nError: {e}")
            print("Please check your API key and internet connection.")
            break

if __name__ == "__main__":
    simple_chatbot()
