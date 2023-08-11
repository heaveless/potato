import os
from dotenv import load_dotenv

load_dotenv()

# --- GLOBAL VARS ---

CORS_ORIGIN = os.getenv("CORS_ORIGIN")