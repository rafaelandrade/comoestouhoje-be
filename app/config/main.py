from os import environ
from app.config.development import development
from app.config.production import production

config = {}

if environ.get('ENV_SERVICE') == 'production':
    config = production(config=config)

if environ.get('ENV_SERVICE') == 'development':
    config = development(config=config)
