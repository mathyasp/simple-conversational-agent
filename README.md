# ACS-4220 AI Engineering & Frameworks
## Simple Conversational Agent

### Getting started:
- Clone this repo
- Start a virtual environment:
  ```bash
  python3 -m venv venv
  source venv/bin/activate  # On Mac/Linux
  ```
- Install required packages:
  ```bash
  python3 -m pip install langchain-openai langchain-core python-dotenv
  ```
- Create a `.env` file
- Using your own API key, add the key to a variable named `OPENAI_API_KEY`:
  ```env
  OPENAI_API_KEY=your-api-key-here
  ```
- Start the agent by running:
  ```bash
  python3 agent.py
  ```

### Using the agent:
- After you start the agent, you will see instructions printed in the terminal:
```bash
Chat started. Commands available:
- 'quit' to exit
- 'history' to see conversation history
- '/mode list' to see available personalities
- '/mode <personality>' to switch personality
```
- The personality options are as follows:
  - **helper**: You are a helpful AI assistant who provides clear and concise answers
  - **teacher**: You are a patient teacher who explains concepts step by step using examples and analogies
  - **coder**: You are a programming expert who writes clean code examples and explains best practices
  - **poet**: You are a poetic soul who responds with creative and lyrical language
  - **chef**: You are a passionate chef who loves talking about food and sharing cooking tips
  - **scientist**: You are a scientist who explains things with precision and references to research

### Example usage:
```bash
You: /mode list
Available personalities:
- helper: You are a helpful AI assistant who provides clear and concise answers
- teacher: You are a patient teacher who explains concepts step by step
...

You: /mode teacher
Switched to teacher personality!

You: How does a binary search work?
AI: Let me explain binary search step by step...
```