import os.path

from pydantic import BaseSettings


class Settings(BaseSettings):
    """
    This would handle the whole settings for the application
    It would, for now, handle the app id an the primary certificate.

    Just make sure that a .env file exists in the base directory of the project
    """
    APP_ID: str
    PRIMARY_CERTIFICATE: str

    class Config:
        env_file = os.path.join(os.getcwd(), '.env')


settings = Settings()
