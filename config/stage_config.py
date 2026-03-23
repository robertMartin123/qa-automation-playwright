# config/stage_config.py

from .base_config import BaseConfig

class StageConfig(BaseConfig):
    BASE_URL = "https://stage.example.com"
    HEADLESS = True
