import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
    TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    DATABASE_URI = os.getenv('DATABASE_URI', 'postgresql://user:password@localhost:5432/ai_phone_agent')
