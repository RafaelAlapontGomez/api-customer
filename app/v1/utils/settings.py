import os

from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    _db_name: str = os.getenv('DATABASE_NAME')

    @property
    def db_name(self):
        if os.getenv('RUN_ENV') == 'test':
            return 'test_' + self._db_name

        return self._db_name
