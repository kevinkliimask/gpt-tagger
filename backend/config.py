from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    frontend_url: str
    chatgpt_api_key: str
    # google_application_credentials: str
    deepl_auth_key: str


settings = Settings()
