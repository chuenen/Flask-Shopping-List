import pytest

from project.app import create_app


@pytest.fixture
def app():
    from project._config import Config
    config = Config({})
    app = create_app(config)
    return app

@pytest.fixture
def client(app):
    return app.test_client()


# vi:et:ts=4:sw=4:cc=80
