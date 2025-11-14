import os
from dotenv import load_dotenv
load_dotenv()
from google.genai import types


api_key = os.environ.get("GEMINI_API_KEY")
from google import genai
client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
)
print(response.text)
# Accessing the specific counts
usage = response.usage_metadata
prompt_tokens = usage.prompt_token_count
response_tokens = usage.candidates_token_count 

print(f"Tokens in Prompt: {prompt_tokens}")
print(f"Tokens in Response: {response_tokens}")