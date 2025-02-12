from flask import Flask
from .utils.database import db

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    # Initialize database
    db.init_app(app)
    
    # Register API routes
    from .api.voice_response import voice_response_bp
    app.register_blueprint(voice_response_bp)
    
    return app
