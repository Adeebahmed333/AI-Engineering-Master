# Import the OpenAI library
from openai import OpenAI

# Initialize the client with your API key
# REPLACE 'your-api-key-here' with your actual key
client = OpenAI(api_key='Dummy')

# Store conversation history
messages = [
    {"role": "system", "content": "You are a helpful AI assistant."}
]

print("AI Chatbot (type 'quit' to exit)")
print("-" * 40)

# Main chat loop
while True:
    # Get user input
    user_input = input("\nYou: ")
    
    # Exit condition
    if user_input.lower() == 'quit':
        print("Goodbye!")
        break
    
    # Add user message to history
    messages.append({"role": "user", "content": user_input})
    
    # Get AI response
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )
    
    # Extract AI's reply
    ai_reply = response.choices[0].message.content
    
    # Add AI reply to history
    messages.append({"role": "assistant", "content": ai_reply})
    
    # Print AI's response
    print(f"\nAI: {ai_reply}")