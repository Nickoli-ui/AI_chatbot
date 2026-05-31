# AI Chatbot with Memory

A conversational AI chatbot that runs completely locally using Ollama and Llama 3.2.

## How it works
Each message is stored in a conversation history list and sent with every 
request — giving the model memory of the full conversation without any 
external database.

## Tech stack
- Python
- Ollama (local LLM runner)
- Llama 3.2 (Meta's open source model)
- OpenAI Python SDK (Ollama compatible)

## Setup
1. Install [Ollama](https://ollama.com) and run `ollama pull llama3.2`
2. Install dependencies: `pip install -r requirements.txt`
3. Run: `python src/chatbot.py`