from openai import OpenAI

# Connect to Ollama running locally on your machine
# Ollama mimics the OpenAI API format so we can use the same library
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",  # Ollama doesn't need a real key, but the library requires one
)

# This list is the memory — every message gets appended here
# and sent with every request so the model can see the full history
conversation_history = []

SYSTEM_PROMPT = """You are a helpful, friendly assistant. 
You remember everything said earlier in the conversation."""

def chat(user_message):
    # Add the user's message to history before sending
    conversation_history.append({
        "role": "user",
        "content": user_message
    })

    # Send the full conversation history every time — this is what creates memory
    response = client.chat.completions.create(
        model="llama3.2",
        messages=[{"role": "system", "content": SYSTEM_PROMPT}] + conversation_history
    )

    # Extract just the text from the response
    assistant_message = response.choices[0].message.content

    # Add the assistant's reply to history so future turns remember it
    conversation_history.append({
        "role": "assistant",
        "content": assistant_message
    })

    return assistant_message


def main():
    print("Chatbot ready. Type 'quit' to exit.\n")

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            continue
        if user_input.lower() == "quit":
            print("Goodbye!")
            break

        response = chat(user_input)
        print(f"\nAssistant: {response}\n")


if __name__ == "__main__":
    main()