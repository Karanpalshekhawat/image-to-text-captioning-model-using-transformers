import os
import configparser

from logging import getLogger

logger = getLogger('[app_running]').getChild('[Downloading_images]')


class Config(object):
    SOURCE_ROOT_DIRECTORY = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))

    def __init__(self, env, cob):
        config = configparser.ConfigParser()
        config.read(os.path.join(os.path.dirname(__file__), 'input.properties'))
        self.propstore_properties = config['Propstore']  # system = self.config.get('Propstore', system')
        self.env = env
        self.cob = cob

    @property
    def system(self):
        return self.propstore_properties.get('system')

    @property
    def grid_app_name(self):
        return self.propstore_properties.get('app_name')

    @property
    def grid_app_version(self):
        return self.propstore_properties.get('app_version')


class GlobalProperties:
    _prop = None
    _cob = None

    @classmethod
    def initialize(cls, env, cob):
        prop = Config(env, cob)
        cls._prop = prop
        return cls._prop


def main():
    GlobalProperties.initialize('dev')


if __name__ == "__main__":
    main()
