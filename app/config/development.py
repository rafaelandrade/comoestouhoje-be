from dotenv import load_dotenv
from os import environ

load_dotenv()


def development(config: dict) -> dict:
    config['ADMIN_TOKEN'] = environ.get('ADMIN_TOKEN')

    return config
