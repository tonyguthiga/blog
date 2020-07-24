import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moring:Access@localhost/blogs'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SECRET_KEY = '~\xb4\xc2\xff\x9fuZ\xa4D\xbe\x7f\xca'
    UPLOADED_PHOTOS_DEST ='app/static/photos'

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}