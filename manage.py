import os
class Config:
   SECRET_KEY = ('vote')
   SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://sylviah:sly@localhost/ivote'
   UPLOADED_PHOTOS_DEST ='app/static/photos'
   MAIL_SERVER = 'smtp.googlemail.com'
   MAIL_PORT = 587
   MAIL_USE_TLS = True
   SQLALCHEMY_TRACK_MODIFICATIONS=True
   MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
   MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
   SIMPLEMDE_JS_IIFE = True
   SIMPLEMDE_USE_CDN = True
class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://sylviah:sly@localhost/ivote'
class TestConfig(Config):
   SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://sylviah:sly@localhost/ivote_test'
class DevConfig(Config):
   SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://sylviah:sly@localhost/ivote'
   DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}