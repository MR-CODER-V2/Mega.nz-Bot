import os


class Config(object):
    APP_ID = int(os.environ.get("APP_ID", "9544521"))
    API_HASH = os.environ.get("API_HASH", "5cf32e97dc94510e46524f2286c95116")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6075048694:AAH9qfXslThzMXCnqAMkaR0UOssufOCi1N0")
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1358657527").split())
    IS_PUBLIC_BOT = os.environ.get("IS_PUBLIC_BOT") in ["false", "false"]
    LOGS_CHANNEL = int(os.environ.get("LOGS_CHANNEL", "-1001411439586")) if os.environ.get("LOGS_CHANNEL") else None
    # DON'T CHANGE THESE 2 VARS
    DOWNLOAD_LOCATION = "./NexaBots"
    TG_MAX_SIZE = 20401084210000000
    # Mega User Account
    MEGA_EMAIL = os.environ.get("MEGA_EMAIL")
    MEGA_PASSWORD = os.environ.get("MEGA_PASSWORD")
