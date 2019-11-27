import os
class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.environ.get='123'
    SQLAlchemy_DATABASE_URI='postgresql+psycopg2://audrey:audrey@localhost/pitches'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME ='mitchelaudrey@gmail.com'
    MAIL_PASSWORD = '123'
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://audrey:audrey@localhost/pitches_test'

class DevConfig(Config):

    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://audrey:audrey@localhost/pitches'
 
    DEBUG = True   

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}     