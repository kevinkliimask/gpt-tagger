from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "ChatGPT powered dataset tagging service"
    chatgpt_api_key: str


settings = Settings()