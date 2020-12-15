import os

import yaml


class Config:

    def __init__(self, settings):
        self._settings = settings

    @property
    def secret_key(self):
        return self._settings.get('secret_key')

    @property
    def host(self):
        return self._settings['host']

    @property
    def seconds(self):
        return self._settings['seconds']

    @property
    def slack_webhook(self):
        return self._settings['slack_webhook']

    @property
    def sqlalchemy_database_url(self):
        return 'mysql+pymysql://%(username)s:%(password)s' \
               '@%(host)s/%(database)s?charset=utf8mb4' \
               % self._settings['mysql']


def config():
    env = os.environ
    with open(env['SETTINGS_PATH']) as ymlfile:
        settings = yaml.load(ymlfile, Loader=yaml.FullLoader)

    return Config(settings)

config = config()


# vi:et:ts=4:sw=4:cc=80
