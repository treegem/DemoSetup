import os
from configparser import ConfigParser

FILE_PATH = os.path.dirname(__file__)
PROJECT_PATH = os.path.join(FILE_PATH, '..')

config = ConfigParser()
config.read(os.path.join(PROJECT_PATH, 'config.ini'))

paths = config['paths']
