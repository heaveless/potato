import os
from dotenv import load_dotenv

load_dotenv()

# --- GLOBAL VARS ---

CORS_ORIGIN = os.getenv("CORS_ORIGIN")

# --- MEGA NZ VARS ---

MEGA_NZ_USERNAME=os.getenv("MEGA_NZ_USERNAME")
MEGA_NZ_PASSWORD=os.getenv("MEGA_NZ_PASSWORD")