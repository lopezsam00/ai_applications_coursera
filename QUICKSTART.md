# Quick Start Guide

Get up and running with AI applications in 5 minutes!

## Step 1: Get Your API Key

1. Go to [OpenAI's website](https://platform.openai.com)
2. Sign up or log in
3. Navigate to API Keys section
4. Click "Create new secret key"
5. Copy your API key (you won't see it again!)

## Step 2: Set Up Your Environment

```bash
# Clone the repository (if not already done)
git clone https://github.com/lopezsam00/ai_applications_coursera.git
cd ai_applications_coursera

# Install Python dependencies
pip install -r requirements.txt

# Create your .env file
cp .env.template .env
```

## Step 3: Add Your API Key

Open the `.env` file in a text editor and replace `your_openai_api_key_here` with your actual API key:

```
OPENAI_API_KEY=sk-...your-actual-key-here...
```

⚠️ **Important**: Never share your API key or commit the `.env` file to Git!

## Step 4: Run Your First Example

```bash
# Try the simple chatbot
python examples/01_simple_chatbot.py
```

Type a message and press Enter to chat with the AI. Type `quit` to exit.

## Step 5: Explore More

### Try Different Examples

```bash
# Text generation with various prompts
python examples/02_text_generation.py

# Document Q&A system
python examples/03_document_qa.py

# Learn prompt engineering
python examples/04_prompt_engineering.py
```

### Use Jupyter Notebooks

```bash
# Start Jupyter
jupyter notebook

# Open: notebooks/01_getting_started.ipynb
```

## Common Issues

### "Module not found" Error

Make sure you've installed the requirements:
```bash
pip install -r requirements.txt
```

### "API Key not found" Error

1. Check that `.env` file exists in the project root
2. Verify your API key is correctly set in `.env`
3. Make sure there are no extra spaces or quotes around the key

### "Rate limit exceeded" Error

You've hit OpenAI's usage limits. Options:
- Wait a few minutes and try again
- Check your OpenAI account for billing status
- Reduce the number of requests

## Next Steps

- 📖 Read the full [README.md](README.md) for detailed documentation
- 💻 Modify the examples to suit your needs
- 🎓 Follow along with your Coursera course
- 🚀 Build your own AI application!

## Getting Help

- Check the [OpenAI documentation](https://platform.openai.com/docs)
- Review error messages carefully (they're usually helpful!)
- Make sure you're using Python 3.8 or higher

---

**Ready to build something amazing? Let's go! 🎉**
