from openai import OpenAI
import os

# --- Configuration ---
# ✅ Make sure you have set your API key in your environment variables.
# For example, in PowerShell: $env:OPENAI_API_KEY="your_secret_key_here"
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# --- API Call ---
try:
    # NOTE: Using 'gpt-4o-mini' as it is the most cost-effective and
    # generally available model, allowing you to test the API for free/cheaply.
    completion = client.chat.completions.create(
        model="gpt-4o-mini", 
        messages=[
            {"role": "system", "content": "You are a virtual assistant named Jarvis, skilled in general tasks like Alexa and Google Assistant."},
            {"role": "user", "content": "What is coding? Keep your answer brief and professional."}
        ]
    )

    # --- Output ---
    print("--- Jarvis's Response ---")
    print(completion.choices[0].message.content)

except Exception as e:
    # This block will catch the 'insufficient_quota' error, but uses a general error message
    print(f"An error occurred during the API call: {e}")
    print("\n💡 Action Required: Please check your OpenAI billing page.")
    print("The API key likely has insufficient credit or has reached a spending limit.")