from openai import AsyncOpenAI

from config.settings import OPENAI_API_KEY

def get_openai_client():
    return AsyncOpenAI(api_key=OPENAI_API_KEY)