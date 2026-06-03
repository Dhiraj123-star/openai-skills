import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable is not set or empty.")

MODEL_NAME = "gpt-5.2"

SKILL_FILE_PATH = "my_skill/SKILL.md"

SKILL_PROPAGATION_WAIT = 5