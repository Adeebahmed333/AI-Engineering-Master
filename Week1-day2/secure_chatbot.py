import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key from environment (NOT hardcoded!)
api_key = os.getenv('OPENAI_API_KEY')

# Check if key exists
if not api_key:
    print("ERROR: OPENAI_API_KEY not found in .env file!")
    exit()

# Initialize client
client = OpenAI(api_key=api_key)

# Test it works
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "Say 'API key loaded successfully!'"}
    ]
)

print(response.choices[0].message.content)