from google import genai
from dotenv import load_dotenv
import os

load_dotenv()  # loads .env into environment

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_response(query: str):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=query,
    )
    return response.text

# if __name__ == "__main__":
#     print(generate_response("Explain the theory of relativity in simple terms."))
