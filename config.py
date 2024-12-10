import os

class Config:
    # Database settings
    DATABASE_HOST = os.environ.get('DATABASE_HOST', '127.0.0.1')
    DATABASE_USER = os.environ.get('DATABASE_USER', 'root')
    DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD', 'admin')
    DATABASE_NAME = os.environ.get('DATABASE_NAME', 'ameerpetstationwithrating')

    # Google Maps API Key
    GOOGLE_MAPS_API_KEY = os.environ.get('GOOGLE_MAPS_API_KEY', 'AIzaSyAb3441ZSzyHBhjWdA0_5mh0hsYDOM0oD0')

    # Flask settings
    DEBUG = os.environ.get('FLASK_DEBUG', 'False') == 'True'


