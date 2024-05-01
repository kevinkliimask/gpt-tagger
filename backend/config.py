from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    frontend_url: str
    chatgpt_api_key: str
    deepl_auth_key: str


settings = Settings()
