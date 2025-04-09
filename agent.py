from langchain_openai import ChatOpenAI
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import os
from dotenv import load_dotenv
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')

llm = ChatOpenAI(model="gpt-3.5-turbo", max_tokens=1000, temperature=0)

store = {}

def get_chat_history(session_id: str):
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

PERSONALITIES = {
    "helper": "You are a helpful AI assistant who provides clear and concise answers.",
    "teacher": "You are a patient teacher who explains concepts step by step using examples and analogies.",
    "coder": "You are a programming expert who writes clean code examples and explains best practices.",
    "poet": "You are a poetic soul who responds with creative and lyrical language.",
    "chef": "You are a passionate chef who loves talking about food and sharing cooking tips.",
    "scientist": "You are a scientist who explains things with precision and references to research."
}

def list_personalities():
    print("\nAvailable personalities:")
    for key, desc in PERSONALITIES.items():
        print(f"- {key}: {desc.split('.')[0]}")

def switch_personality(personality_key):
    global prompt, chain, chain_with_history
    if personality_key == "list":
        list_personalities()
        return ""
    if personality_key in PERSONALITIES:
        prompt = ChatPromptTemplate.from_messages([
            ("system", PERSONALITIES[personality_key]),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{input}")
        ])
        chain = prompt | llm
        chain_with_history = RunnableWithMessageHistory(
            chain,
            get_chat_history,
            input_messages_key="input",
            history_messages_key="history"
        )
        return f"Switched to {personality_key} personality!"
    return f"Invalid personality. Use '/mode list' to see available options."

prompt = ChatPromptTemplate.from_messages([
    ("system", PERSONALITIES["helper"]),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])

chain = prompt | llm

chain_with_history = RunnableWithMessageHistory(
    chain,
    get_chat_history,
    input_messages_key="input",
    history_messages_key="history"
)

session_id = "user_123"

def print_conversation_history(session_id):
    if session_id in store:
        print("\nConversation History:")
        for message in store[session_id].messages:
            sender = "User" if message.type == "human" else "AI"
            print(f"{sender}: {message.content}")
    else:
        print("No conversation history found")

def chat():
    print("Chat started. Commands available:")
    print("- 'quit' to exit")
    print("- 'history' to see conversation history")
    print("- '/mode list' to see available personalities")
    print("- '/mode <personality>' to switch personality")
    
    while True:
        user_input = input("\nYou: ").strip()
        
        if user_input.lower() == 'quit':
            break
        elif user_input.lower() == 'history':
            print_conversation_history(session_id)
            continue
        elif user_input.startswith('/mode '):
            personality = user_input.split(' ')[1].lower()
            response = switch_personality(personality)
            if response:  # Only print if there's a response
                print(response)
            continue
        
        response = chain_with_history.invoke(
            {"input": user_input},
            config={"configurable": {"session_id": session_id}}
        )
        print("AI:", response.content)

if __name__ == "__main__":
    chat()