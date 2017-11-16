import os
from configparser import ConfigParser

config = ConfigParser()

FILE_PATH = os.path.dirname(__file__)
PROJECT_PATH = os.path.join(FILE_PATH, '..')

# PATHS
config['paths'] = {}
config['paths']['project'] = PROJECT_PATH
config['paths']['saves'] = os.path.join(PROJECT_PATH, 'saves')

with open(os.path.join(PROJECT_PATH, 'config.ini'), 'w') as conf:
    config.write(conf)
