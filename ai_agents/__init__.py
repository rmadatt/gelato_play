# __init__.py
from flask import Flask
from .config import Config
from .views import bp as views_bp  # Import blueprint from views

def create_app():
    """Initialize and configure the Flask application."""
    app = Flask(__name__)
    app.config.from_object(Config)  # Load configuration from config.py
    
    # Register blueprints (routes/views)
    app.register_blueprint(views_bp)
    
    return app

# Create the app instance
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)  # Run in debug mode for development
