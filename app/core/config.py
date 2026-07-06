import os
from dotenv import load_dotenv

load_dotenv()


class Config:

    APP_NAME = os.getenv("APP_NAME", "Atlas")

    VERSION = os.getenv("VERSION", "0.2.0-alpha")

    SECRET_KEY = os.getenv("SECRET_KEY", "development")

    WORKBOOK_PATH = os.getenv("WORKBOOK_PATH")
