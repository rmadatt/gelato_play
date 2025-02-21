# config.py
import os

class Config:
    """Base configuration for Gelato Play."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key-here')  # Change this in production
    DEBUG = True  # Set to False in production
    FLASK_ENV = 'development'  # Switch to 'production' later
    TEMPLATES_AUTO_RELOAD = True  # Auto-reload templates during development

# config.py
import os
from datetime import timedelta

class Config:
    """Base configuration class."""
    # Flask Core Settings
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-please-change-in-production'
    
    # Security Settings
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    PERMANENT_SESSION_LIFETIME = timedelta(days=1)
    
    # Database Settings (example with PostgreSQL)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Redis Settings (for caching and rate limiting)
    REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379/0')
    
    # Email Settings (if using email functionality)
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', 587))
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    
    # File Upload Settings
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    UPLOAD_FOLDER = 'uploads'
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'pdf'}

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    DEVELOPMENT = True
    # Override with local development settings
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'
    # Less strict security for development
    SESSION_COOKIE_SECURE = False

class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    TESTING = False
    # Ensure all security features are enabled
    SESSION_COOKIE_SECURE = True
    PREFERRED_URL_SCHEME = 'https'

class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True
    # Use a separate test database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    # Disable CSRF tokens in testing
    WTF_CSRF_ENABLED = False

# Dictionary to easily access different configs
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}

Copy

Insert at cursor
python
Then in your __init__.py, you would use it like this:

# __init__.py
from flask import Flask
from .config import config
import os

def create_app(config_name=None):
    """Application factory function."""
    if config_name is None:
        config_name = os.environ.get('FLASK_ENV', 'default')
    
    app = Flask(__name__)
    
    # Load the config
    app.config.from_object(config[config_name])
    
    # Initialize extensions
    # db.init_app(app)
    # mail.init_app(app)
    # etc...
    
    return app

Copy

Insert at cursor
python
Key points about config.py:

Environment Variables :

SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-please-change-in-production'

Copy

Insert at cursor
python
Always use environment variables for sensitive information

Provide fallback values only for development

Different Environments :

class DevelopmentConfig(Config):
    DEBUG = True
    
class ProductionConfig(Config):
    DEBUG = False

Copy

Insert at cursor
python
Separate configurations for development, testing, and production

Each environment inherits from base Config class

Common Settings Categories :

Security settings (SECRET_KEY, cookie settings)

Database connections

Email settings

File upload configurations

API keys and external service configurations

Caching settings

Logging configurations

Best Practices :

# Good: Using environment variables
DATABASE_URL = os.environ.get('DATABASE_URL')

# Good: Different settings per environment
class ProductionConfig(Config):
    SESSION_COOKIE_SECURE = True
    
# Good: Reasonable defaults with overrides
MAIL_PORT = int(os.environ.get('MAIL_PORT', 587))

Copy

Insert at cursor
python
To use this configuration:

Set environment variables:

export FLASK_ENV=development
export SECRET_KEY=your-secret-key
export DATABASE_URL=postgresql://user:pass@localhost/dbname

Copy

Insert at cursor
bash
Create a .env file for development:

FLASK_ENV=development
SECRET_KEY=dev-secret-key
DATABASE_URL=postgresql://localhost/dev_db

Copy

Insert at cursor
env
Use different settings in different environments:

# Development
app = create_app('development')

# Production
app = create_app('production')

# Testing
app = create_app('testing')

Copy

Insert at cursor
python
This configuration structure:

Keeps sensitive data secure

Makes it easy to switch between environments

Provides clear separation of concerns

Makes the application more maintainable

Follows Flask best practices
