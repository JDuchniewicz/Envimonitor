"""Flask app routes."""
from flask import render_template
from flask import current_app as app

@app.route('/')
def home():
    """Landing page.""" # TODO: this will be the dashboard (not home-template)
    return render_template('index.jinja2',
                           title='Envimonitor',
                           template='home-template',
                           body="Welcome to envimonitor lol."
                           )
# TODO: add routes, dash apps will be in some of them
# rest will be static control pages
