from flask import Flask, jsonify


def create_app(config):
    app = Flask(__name__)
    app.config.update(
        SECRET_KEY=config.secret_key,
    )

    from .web.views import web
    from .api import api
    app.register_blueprint(web)
    app.register_blueprint(api)

    return app


# vi:et:ts=4:sw=4:cc=80
