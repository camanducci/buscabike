from dynaconf.contrib.flask_dynaconf import FlaskDynaconf


def configure(app):
    """Configure Dynaconf Flask Extension"""
    FlaskDynaconf(
        app=app,
        DYNACONF_NAMESPACE='BUSCABIKE',
        SETTINGS_MODULE=f'{app.root_path}/settings.yml'
    )
