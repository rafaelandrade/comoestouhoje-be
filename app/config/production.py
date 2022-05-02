from dotenv import load_dotenv
from os import environ

load_dotenv()


def production(config: dict) -> dict:
    config['ADMIN_TOKEN'] = environ.get('ADMIN_TOKEN')
    config['SENTRY_DSN'] = environ.get('SENTRY_DSN')

    return config
