#----------------------------------- https://github.com/m4mallu/clonebot --------------------------------------------#
import os
import logging
config.fp16 = False

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6073974860:AAEjfC0SV8W4L9wnrTR1tII4C2pz9qgPzmI")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "904789"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "2262ef67ced426b9eea57867b11666a1")

    # Generate a user session string
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQANzlUAKJzhB5JB7b2G2QkLwqwOqEkLKkibddOWaebMjevOiK3Rfndt5tYF10HgVzGimAnsY7TNR7tXviTA5tk-l10S8X4ZDO3WWAZUMA2fiSVKcU64KxFYhYtA0BcyRmjzHP9AzeWEJiLJyk8zPjFkWPGtDshbcjZ-r5c_h6MKdyl2x0Mr_IrKppQTl4uzZ-gDc64qmMfn-XfTAiKOtUhRTg05npEhQLj6J_evEFbZZyrV-jcbeQx9M8UoICTlSoMfAkTIKqOsSIQ0Agon5aSu948D3CIfd6RqXMMlBa7eRLpUz0wc5opskR8tfGQLgBUJK687vjrNDvN9ThM4at60Nds4vQAAAAA7zbY8AA")

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "postgresql://SURAJ:878@localhost:5432/SURAJ.878")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
