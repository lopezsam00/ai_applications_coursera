# AI Applications Coursera - Project Repository

This repository contains practice projects and examples for the **IBM Generative AI Applications** course on Coursera. Follow along with hands-on examples to learn how to build real-world AI applications.

## 📚 What's Included

- **Example Scripts**: Ready-to-run Python scripts demonstrating key concepts
- **Jupyter Notebooks**: Interactive tutorials for learning
- **Utilities**: Configuration and helper functions
- **Documentation**: Setup instructions and best practices

## 🚀 Quick Start

### 1. Prerequisites

- Python 3.8 or higher
- An OpenAI API key ([Get one here](https://platform.openai.com/api-keys))
- Basic knowledge of Python

### 2. Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/lopezsam00/ai_applications_coursera.git
cd ai_applications_coursera
pip install -r requirements.txt
```

### 3. Configuration

1. Copy the environment template:
   ```bash
   cp .env.template .env
   ```

2. Edit `.env` and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_actual_api_key_here
   ```

3. (Optional) Adjust other settings like model, temperature, etc.

### 4. Run Examples

Try the example scripts:

```bash
# Simple chatbot
python examples/01_simple_chatbot.py

# Text generation with different prompts
python examples/02_text_generation.py

# Document Q&A system
python examples/03_document_qa.py
```

### 5. Explore Notebooks

Launch Jupyter to explore interactive tutorials:

```bash
jupyter notebook notebooks/01_getting_started.ipynb
```

## 📁 Project Structure

```
ai_applications_coursera/
├── examples/              # Example Python scripts
│   ├── 01_simple_chatbot.py
│   ├── 02_text_generation.py
│   ├── 03_document_qa.py
│   └── 04_prompt_engineering.py
├── notebooks/             # Jupyter notebooks
│   └── 01_getting_started.ipynb
├── utils/                 # Utility functions
│   ├── __init__.py
│   └── config.py
├── .env.template          # Environment variables template
├── .gitignore            # Git ignore rules
├── requirements.txt       # Python dependencies
├── QUICKSTART.md         # Quick start guide
└── README.md             # This file
```

## 🎓 Learning Path

1. **Start with the basics**: Run `examples/01_simple_chatbot.py` to understand API calls
2. **Learn prompt engineering**: Explore `examples/02_text_generation.py`
3. **Build Q&A systems**: Try `examples/03_document_qa.py`
4. **Interactive learning**: Open `notebooks/01_getting_started.ipynb`
5. **Experiment**: Modify the examples and create your own projects!

## 🔑 Key Concepts Covered

- **Large Language Models (LLMs)**: Understanding and using GPT models
- **Prompt Engineering**: Crafting effective prompts for better results
- **API Integration**: Working with OpenAI's API
- **Temperature Control**: Balancing creativity and determinism
- **Conversation Management**: Building chatbots with memory
- **Document Q&A**: Creating context-aware AI systems

## 💡 Tips for Success

1. **Start Simple**: Begin with basic examples before building complex applications
2. **Experiment**: Try different prompts, temperatures, and parameters
3. **Manage Costs**: Monitor your API usage on the OpenAI dashboard
4. **Read Errors**: Error messages often contain helpful debugging information
5. **Iterate**: AI development is iterative - refine your prompts based on results

## 🔒 Security Best Practices

- Never commit your `.env` file or API keys to version control
- Use environment variables for sensitive data
- Monitor API usage to avoid unexpected charges
- Rotate API keys periodically
- Review OpenAI's usage policies and guidelines

## 📖 Additional Resources

- [OpenAI API Documentation](https://platform.openai.com/docs)
- [OpenAI Cookbook](https://github.com/openai/openai-cookbook)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)
- [IBM AI Resources](https://www.ibm.com/artificial-intelligence)

## 🤝 Contributing

Feel free to:
- Add your own examples
- Improve documentation
- Share interesting use cases
- Report issues or bugs

## 📝 License

This is a learning project for personal and educational use.

## ⚠️ Disclaimer

This project is for educational purposes. API usage may incur costs. Always review OpenAI's pricing and terms of service.

---

**Happy Learning! 🎉**
