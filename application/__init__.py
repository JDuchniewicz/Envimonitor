"""Initialize Flask app."""
from flask import Flask
from flask_assets import Environment
from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS

client = InfluxDBClient.from_env_properties()
write_api = client.write_api(write_options=SYNCHRONOUS)
query_api = client.query_api()

def create_app():
    """Construct Flask application with embedded Dash app."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    assets = Environment()
    assets.init_app(app)

    with app.app_context():
        from application import routes
        from application.dashboard import create_dashboard
        app = create_dashboard(app)

        # compile static assets
        from application.assets import compile_static_assets
        compile_static_assets(assets)

        return app
