from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OPENAI_CHAT_MODEL = os.getenv("OPENAI_CHAT_MODEL")
    OPENAI_EMBEDDING_MODEL = os.getenv("OPENAI_EMBEDDING_MODEL")

settings = Settings()

print("OpenAI API Key:", settings.OPENAI_API_KEY)
print("OpenAI Chat Model:", settings.OPENAI_CHAT_MODEL)