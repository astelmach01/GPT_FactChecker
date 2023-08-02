from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    API_V1_STR: str
    project_name: str
    environment: str

    openai_api_key: str
    openai_organization: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
