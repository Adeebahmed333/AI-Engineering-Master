import os
from openai import OpenAI
from dotenv import load_dotenv
import time

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def chat_with_retry(messages, max_retries=3):
    """
    Chat with automatic retry on failure
    """
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages,
                timeout=30  # Wait max 30 seconds
            )
            return response.choices[0].message.content
            
        except Exception as e:
            print(f"\n⚠️  Attempt {attempt + 1} failed: {str(e)}")
            
            if attempt < max_retries - 1:
                wait_time = 2 ** attempt  # Exponential backoff: 1s, 2s, 4s
                print(f"⏳ Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                print("❌ All retries failed!")
                return None

# Main chatbot
messages = [{"role": "system", "content": "You are a helpful assistant."}]

print("🤖 Robust AI Chatbot")
print("=" * 50)
print("Type 'quit' to exit\n")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == 'quit':
        print("\n👋 Goodbye!")
        break
    
    if not user_input.strip():
        print("⚠️  Please enter a message!")
        continue
    
    messages.append({"role": "user", "content": user_input})
    
    print("\n🤔 Thinking...", end='', flush=True)
    
    ai_reply = chat_with_retry(messages)
    
    if ai_reply:
        messages.append({"role": "assistant", "content": ai_reply})
        print(f"\r✨ AI: {ai_reply}\n")
    else:
        print("\r❌ Sorry, I couldn't process that. Try again.\n")
        messages.pop()  # Remove failed user message