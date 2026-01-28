"""
Example 3: Simple Document Q&A System

This example demonstrates:
- Reading and processing documents
- Creating a simple Q&A system
- Using context to answer questions
"""

import sys
from pathlib import Path

# Add project root to path for imports
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from openai import OpenAI
from utils.config import config

def create_sample_document():
    """Create a sample document for demonstration."""
    return """
    Generative AI Course Overview
    
    This course covers the fundamentals of developing applications with Generative AI.
    You will learn about:
    
    1. Large Language Models (LLMs): Understanding how models like GPT work and how to use them.
    
    2. Prompt Engineering: Crafting effective prompts to get the best results from AI models.
    
    3. API Integration: Connecting to AI services like OpenAI's API to build real applications.
    
    4. Use Cases: Chatbots, content generation, summarization, translation, and code generation.
    
    5. Best Practices: Managing API costs, handling errors, and ensuring responsible AI use.
    
    Prerequisites: Basic Python programming knowledge and familiarity with APIs.
    Duration: 4 weeks with hands-on projects.
    """

def answer_question(document, question):
    """Answer a question based on the provided document."""
    
    # Validate configuration
    try:
        config.validate()
    except ValueError as e:
        print(f"Configuration Error: {e}")
        return None
    
    # Initialize OpenAI client
    client = OpenAI(api_key=config.OPENAI_API_KEY)
    
    # Create a prompt that includes the document and question
    prompt = f"""Based on the following document, answer the question. 
If the answer is not in the document, say "I don't have that information in the document."

Document:
{document}

Question: {question}

Answer:"""
    
    try:
        response = client.chat.completions.create(
            model=config.DEFAULT_MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful assistant that answers questions based on provided documents."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,  # Lower temperature for more factual responses
            max_tokens=300
        )
        
        return response.choices[0].message.content
    
    except Exception as e:
        print(f"Error: {e}")
        return None

def demonstrate_qa_system():
    """Demonstrate the Q&A system."""
    
    print("Document Q&A System")
    print("=" * 60)
    
    # Get sample document
    document = create_sample_document()
    
    print("\n--- Sample Document ---")
    print(document)
    print("\n" + "=" * 60)
    
    # List of questions to ask
    questions = [
        "What topics does the course cover?",
        "What are the prerequisites?",
        "How long is the course?",
        "Does the course cover blockchain?",  # Not in document
    ]
    
    # Ask each question
    for i, question in enumerate(questions, 1):
        print(f"\nQuestion {i}: {question}")
        print("-" * 60)
        answer = answer_question(document, question)
        if answer:
            print(f"Answer: {answer}")
    
    # Interactive mode
    print("\n" + "=" * 60)
    print("\nInteractive Q&A Mode (type 'quit' to exit)")
    print("-" * 60)
    
    while True:
        user_question = input("\nYour question: ").strip()
        
        if user_question.lower() in ['quit', 'exit', 'q']:
            print("Goodbye!")
            break
        
        if not user_question:
            continue
        
        answer = answer_question(document, user_question)
        if answer:
            print(f"\nAnswer: {answer}")

if __name__ == "__main__":
    demonstrate_qa_system()
