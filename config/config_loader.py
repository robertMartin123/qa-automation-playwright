# config/config_loader.py

import os
from config.dev_config import DevConfig
from config.stage_config import StageConfig

def get_config():
    env = os.getenv("TEST_ENV", "dev")

    if env == "stage":
        return StageConfig()
    return DevConfig()
