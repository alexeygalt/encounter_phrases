import os
from pathlib import Path
import environ

BASE_DIR = Path(__file__).resolve().parent

environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

env = environ.Env()

BOT_TOKEN = env.str("BOT_TOKEN", None)
