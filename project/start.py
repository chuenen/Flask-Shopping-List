from . import config
from .app import create_app

application = create_app(config)


# vi:et:ts=4:sw=4:cc=80
