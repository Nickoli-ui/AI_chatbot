import streamlit as st
from openai import OpenAI

# Connect to Ollama running locally on your machine
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",  # Ollama doesn't need a real key, but the library requires one
)

SYSTEM_PROMPT = """You are a helpful, friendly assistant.
You remember everything said earlier in the conversation."""

# st.session_state persists across interactions, so we can use it to store conversation history
# Without this, the chatbot would forget everything after every message
if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = []  
    
st.title("AI Chatbot")
st.caption("Running Locally with Llama 3.2 and Ollama")


# Draw a chat bubble for each message in the conversation history
for message in st.session_state.conversation_history:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# The chat input bar at the bottom of the page
user_input = st.chat_input("Type your message here...")

if user_input:
    # Show the user's message
    with st.chat_message("user"):
        st.write(user_input)

    # Add to history
    st.session_state.conversation_history.append({
        "role": "user",
        "content": user_input
    })

    # Get Response from Ollama
    response = client.chat.completions.create(
        model="llama3.2",
        messages=[{"role": "system", "content": SYSTEM_PROMPT}] + st.session_state.conversation_history
    )

    assistant_message = response.choices[0].message.content

    # Show the assistant's message
    with st.chat_message("assistant"):
        st.write(assistant_message)

    # Add to history
    st.session_state.conversation_history.append({
        "role": "assistant",
        "content": assistant_message
    })

# Sidebar with a reset button to clear conversation history
with st.sidebar:
    st.header("Controls")
    if st.button("Clear Conversation"):
        st.session_state.conversation_history = []
        st.rerun()  # Refresh the page to clear the chat bubbles