"""
Example 4: Prompt Engineering Best Practices

This example demonstrates:
- Different prompting techniques
- How to structure prompts for better results
- Common prompt patterns
"""

from openai import OpenAI
from utils.config import config

def get_completion(prompt, temperature=0.7):
    """Helper function to get completions."""
    try:
        config.validate()
    except ValueError as e:
        print(f"Configuration Error: {e}")
        return None
    
    client = OpenAI(api_key=config.OPENAI_API_KEY)
    
    try:
        response = client.chat.completions.create(
            model=config.DEFAULT_MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error: {e}")
        return None

def demonstrate_prompt_patterns():
    """Demonstrate various prompt engineering patterns."""
    
    print("Prompt Engineering Best Practices")
    print("=" * 70)
    
    # Pattern 1: Clear Instructions
    print("\n1. CLEAR INSTRUCTIONS")
    print("-" * 70)
    print("Bad: Tell me about Python")
    bad_result = get_completion("Tell me about Python")
    print(f"Result: {bad_result}\n")
    
    print("Good: Explain Python programming language in 3 bullet points")
    good_result = get_completion(
        "Explain Python programming language in 3 bullet points, "
        "focusing on its main advantages for beginners."
    )
    print(f"Result: {good_result}")
    
    # Pattern 2: Provide Context
    print("\n2. PROVIDE CONTEXT")
    print("-" * 70)
    context_prompt = """
    Context: You are a technical writer creating documentation for beginners.
    
    Task: Explain what an API is and why it's useful.
    
    Requirements:
    - Use simple language
    - Include a real-world analogy
    - Keep it under 100 words
    """
    result = get_completion(context_prompt, temperature=0.3)
    print(f"Result: {result}")
    
    # Pattern 3: Few-Shot Learning
    print("\n3. FEW-SHOT LEARNING (Learning from Examples)")
    print("-" * 70)
    few_shot_prompt = """
    Convert these sentences to a more professional tone:
    
    Example 1:
    Input: "Hey, can you do this ASAP?"
    Output: "Could you please prioritize this task?"
    
    Example 2:
    Input: "This is broken, fix it!"
    Output: "I've encountered an issue that requires attention."
    
    Now convert this:
    Input: "Your code is a mess"
    Output:
    """
    result = get_completion(few_shot_prompt, temperature=0.3)
    print(f"Result: {result}")
    
    # Pattern 4: Chain of Thought
    print("\n4. CHAIN OF THOUGHT (Step-by-Step Reasoning)")
    print("-" * 70)
    cot_prompt = """
    Problem: A store has 15 apples. They sell 7 apples in the morning and 
    receive a shipment of 12 more apples in the afternoon. How many apples 
    do they have at the end of the day?
    
    Solve this step by step:
    """
    result = get_completion(cot_prompt, temperature=0.2)
    print(f"Result: {result}")
    
    # Pattern 5: Role Assignment
    print("\n5. ROLE ASSIGNMENT")
    print("-" * 70)
    role_prompt = """
    You are an experienced software architect reviewing code.
    
    Code:
    ```python
    def calculate(a, b):
        return a + b
    ```
    
    Provide feedback on:
    1. Code quality
    2. Naming conventions
    3. Documentation
    4. Potential improvements
    """
    result = get_completion(role_prompt, temperature=0.4)
    print(f"Result: {result}")
    
    # Pattern 6: Output Format Specification
    print("\n6. OUTPUT FORMAT SPECIFICATION")
    print("-" * 70)
    format_prompt = """
    List 3 benefits of exercise.
    
    Format your response as JSON with the following structure:
    {
        "benefits": [
            {"benefit": "...", "description": "..."},
            ...
        ]
    }
    """
    result = get_completion(format_prompt, temperature=0.3)
    print(f"Result: {result}")
    
    # Pattern 7: Constraints and Limitations
    print("\n7. CONSTRAINTS AND LIMITATIONS")
    print("-" * 70)
    constraint_prompt = """
    Write a product description for wireless headphones.
    
    Constraints:
    - Exactly 50 words
    - Include the word "premium" at least once
    - End with a call to action
    - Target audience: young professionals
    """
    result = get_completion(constraint_prompt, temperature=0.7)
    print(f"Result: {result}")
    print(f"Word count: {len(result.split())}")

def demonstrate_common_mistakes():
    """Show common prompting mistakes and how to fix them."""
    
    print("\n" + "=" * 70)
    print("COMMON MISTAKES TO AVOID")
    print("=" * 70)
    
    mistakes = [
        {
            "mistake": "Being too vague",
            "bad": "Write something about AI",
            "good": "Write a 100-word introduction to AI for a high school student"
        },
        {
            "mistake": "Multiple unrelated tasks",
            "bad": "Explain AI, write a poem, and calculate 23 * 45",
            "good": "Focus on one task at a time for better results"
        },
        {
            "mistake": "Assuming too much knowledge",
            "bad": "Implement a transformer model",
            "good": "Explain what a transformer model is and provide a simple Python example"
        }
    ]
    
    for i, item in enumerate(mistakes, 1):
        print(f"\nMistake {i}: {item['mistake']}")
        print(f"Bad: {item['bad']}")
        print(f"Good: {item['good']}")

if __name__ == "__main__":
    demonstrate_prompt_patterns()
    demonstrate_common_mistakes()
    
    print("\n" + "=" * 70)
    print("\nKey Takeaways:")
    print("1. Be specific and clear in your instructions")
    print("2. Provide context when needed")
    print("3. Use examples to guide the AI (few-shot learning)")
    print("4. Request step-by-step reasoning for complex tasks")
    print("5. Assign roles to get domain-specific responses")
    print("6. Specify the desired output format")
    print("7. Set constraints to control the output")
    print("=" * 70)
