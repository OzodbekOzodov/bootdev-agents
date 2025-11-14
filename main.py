import os
from dotenv import load_dotenv
load_dotenv()
from google.genai import types
import sys
api_key = os.environ.get("GEMINI_API_KEY")
from google import genai
client = genai.Client(api_key=api_key)

def main(text:str):
    response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents = text
)
    print(response.text)
    # Accessing the specific counts
    usage = response.usage_metadata
    prompt_tokens = usage.prompt_token_count
    response_tokens = usage.candidates_token_count 
    print(f"Prompt tokens: {prompt_tokens}")
    print(f"Response tokens: {response_tokens}")

if __name__ == "__main__":
    text = sys.argv[1]
    main(text)