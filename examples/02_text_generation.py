"""
Example 2: Text Generation with Custom Prompts

This example demonstrates:
- Crafting effective prompts
- Generating different types of content
- Using temperature to control creativity
"""

import sys
from pathlib import Path

# Add project root to path for imports
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from openai import OpenAI
from utils.config import config


def generate_text(prompt, temperature=0.7, max_tokens=500):
    """Generate text based on a prompt."""

    # Validate configuration
    try:
        config.validate()
    except ValueError as e:
        print(f"Configuration Error: {e}")
        return None

    # Initialize OpenAI client
    client = OpenAI(api_key=config.OPENAI_API_KEY)

    try:
        response = client.chat.completions.create(
            model=config.DEFAULT_MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens,
        )

        return response.choices[0].message.content

    except Exception as e:
        print(f"Error generating text: {e}")
        return None


def demonstrate_text_generation():
    """Demonstrate various text generation scenarios."""

    print("Text Generation Examples")
    print("=" * 60)

    # Example 1: Creative writing (high temperature)
    print("\n1. Creative Story (High Temperature = 0.9)")
    print("-" * 60)
    creative_prompt = (
        "Write a short story about a robot learning to paint in exactly 3 sentences."
    )
    result = generate_text(creative_prompt, temperature=0.9, max_tokens=200)
    if result:
        print(result)

    # Example 2: Technical explanation (low temperature)
    print("\n2. Technical Explanation (Low Temperature = 0.2)")
    print("-" * 60)
    technical_prompt = "Explain what machine learning is in simple terms."
    result = generate_text(technical_prompt, temperature=0.2, max_tokens=200)
    if result:
        print(result)

    # Example 3: Code generation
    print("\n3. Code Generation")
    print("-" * 60)
    code_prompt = "Write a Python function to calculate the fibonacci sequence."
    result = generate_text(code_prompt, temperature=0.3, max_tokens=300)
    if result:
        print(result)

    # Example 4: Summarization
    print("\n4. Text Summarization")
    print("-" * 60)
    long_text = """
    Artificial Intelligence (AI) is transforming the way we live and work. 
    Machine learning, a subset of AI, enables computers to learn from data 
    without being explicitly programmed. Deep learning, which uses neural 
    networks with multiple layers, has achieved remarkable results in image 
    recognition, natural language processing, and game playing. Recent 
    advances in generative AI, such as large language models, have made it 
    possible to create human-like text, images, and even code.
    """
    summary_prompt = f"Summarize this text in one sentence: {long_text}"
    result = generate_text(summary_prompt, temperature=0.3, max_tokens=100)
    if result:
        print(result)


if __name__ == "__main__":
    demonstrate_text_generation()
