import os

from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    _db_name: str = os.getenv('DB_DATABASE')
    db_user: str = os.getenv('DB_USER')
    db_pass: str = os.getenv('DB_PASSWORD')
    db_host: str = os.getenv('DB_HOST')
    db_port: int = os.getenv('DB_PORT')

    @property
    def db_name(self):
        if os.getenv('RUN_ENV') == 'test':
            return 'test_' + self._db_name

        return self._db_name
