import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

def categorization():
    client = genai.Client(api_key=GEMINI_API_KEY)
    
    interaction = client.interactions.create(
        model="gemini-3-flash-preview",
        input="explique, em uma frase, o que é python",
        stream= True
    )

    print(interaction.output_text)

categorization()