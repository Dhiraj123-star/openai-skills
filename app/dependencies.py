from openai import AsyncOpenAI

from config.settings import OPENAI_API_KEY

# Instantiate a single global client to enable HTTP connection pooling
# and configure a timeout to prevent requests from hanging indefinitely
_client = AsyncOpenAI(
    api_key=OPENAI_API_KEY,
    timeout=60.0,
)

def get_openai_client() -> AsyncOpenAI:
    return _client