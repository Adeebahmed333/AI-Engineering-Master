from openai import OpenAI

client = OpenAI(api_key='Dummy')

def rewrite_text(text, tone):
    """
    Rewrite text in different tones
    """
    prompt = f"""Rewrite the following text in a {tone} tone:

    Text: {text}

    Rewritten version:"""
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a professional writer."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    
    return response.choices[0].message.content

# Main program
print("AI Writing Assistant")
print("-" * 40)

# Get user input
original_text = input("\nEnter text to rewrite: ")
print("\nAvailable tones: professional, casual, friendly, formal, humorous")
tone = input("Choose tone: ")

# Rewrite
rewritten = rewrite_text(original_text, tone)

# Display results
print("\n" + "="*40)
print("ORIGINAL:")
print(original_text)
print("\n" + "="*40)
print(f"REWRITTEN ({tone.upper()}):")
print(rewritten)