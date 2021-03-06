import os

from configparser import ConfigParser

from utility.create_config import create_config

create_config()

FILE_PATH = os.path.dirname(__file__)
PROJECT_PATH = os.path.join(FILE_PATH, '..')

config = ConfigParser()
config.read(os.path.join(PROJECT_PATH, 'config.ini'))

paths = {}

for key in config['paths'].keys():
    paths[key] = str(config['paths'][key])
