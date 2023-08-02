import openai

from app.settings import settings

openai.api_key = settings.openai_api_key
openai.organization = settings.openai_organization
