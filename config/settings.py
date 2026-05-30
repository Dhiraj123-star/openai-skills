import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY= os.getenv("OPENAI_API_KEY")

MODEL_NAME = "gpt-5.2"

SKILL_NAME = "data-analyzer"

SKILL_FILE_PATH = "my_skill/SKILL.md"

SKILL_PROPAGATION_WAIT = 5