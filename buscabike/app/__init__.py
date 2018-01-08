from flask import Flask

from buscabike import config, ext


def create_app(import_name='buscabike'):
    app = Flask(import_name)

    # Configuration
    config.configure(app)

    # Extensions
    ext.configure(app)

    return app
