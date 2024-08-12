import os
import logging

class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')

class DevelopmentConfig(Config):
    DEBUG = True
    ENV = 'development'
    LOG_LEVEL = logging.DEBUG

class ProductionConfig(Config):
    ENV = 'production'
    LOG_LEVEL = logging.INFO

class TestingConfig(Config):
    TESTING = True
    LOG_LEVEL = logging.DEBUG

def get_config(env):
    if env == 'development':
        return DevelopmentConfig()
    elif env == 'production':
        return ProductionConfig()
    elif env == 'testing':
        return TestingConfig()
    else:
        raise ValueError("Invalid environment name")
