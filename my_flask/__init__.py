import os
from flask import Flask

PKL_FILEPATH = os.path.join(os.getcwd(), __name__, 'ml_pipe.pkl') 

def create_app(config=None):
    app = Flask(__name__)
    
    if config is not None:
        app.config.update(config)
    
    from my_flask.views.main_views import main_bp
    from my_flask.views.api_views import api_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp, url_prefix='/api')

    return app