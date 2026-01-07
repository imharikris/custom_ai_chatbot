from google import genai
import os 
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in environment variables")
client = genai.Client(api_key= GEMINI_API_KEY)

EMBEDDING_MODEL = "gemini-embedding-001"
GENERATIVE_MODEL = "gemini-2.5-flash"