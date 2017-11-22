import os

from configparser import ConfigParser


def create_config():
    config = ConfigParser()

    FILE_PATH = os.path.dirname(__file__)
    PROJECT_PATH = os.path.join(FILE_PATH, '..')

    config['paths'] = {'project': PROJECT_PATH,
                       'saves': os.path.join(PROJECT_PATH, 'saves'),
                       'calibrations': os.path.join(PROJECT_PATH, 'calibrations')
                       }

    with open(os.path.join(PROJECT_PATH, 'config.ini'), 'w') as conf:
        config.write(conf)
