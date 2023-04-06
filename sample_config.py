#----------------------------------- https://github.com/m4mallu/clonebot --------------------------------------------#
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6028638892:AAHCorTms_6f7i3kpdfeToINqyHrRlRxzRg")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "14385287"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "8f7c88b761edf0d3f082fd1b4f53e2e1")

    # Generate a user session string
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQDbgIcAgDIPrCw7zxkJrV5E5MG9tSCeJfteMfgvD-9pjnX4WbVVJ59WLfRIzAOz1HG6zYj2Mm2i0k8PT8yg7Er4wUa4yzHMUZ3AZ1GdaG2Jbo6JQitVxTJs2wKbIGFqcCIbd6kLv7IUPVIfpGlwuz0uKOgfhPuOp29g0vUgsOq0-rcifB2wfuHqB1R5_xXfi5pA6jedtqffT9FdYFkStJNO1hkR35RUEFL04CNa845vMYhJjIpbTuuj9Em4Kag7MuXPpLM7YjuNxpf55ZsRZrafdEWziD0ISL0OuNaNaeHZCZ0grbzO8MNF0O-MNvLoVbGodwSPj-1Z7l97TZqxf1XyF7Z6SwAAAAFCvZv-AA")

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "
mongodb+srv://Surajrathod:Surajrathod.878@cluster0.f8wzeit.mongodb.net/?retryWrites=true&w=majority")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
