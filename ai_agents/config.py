# config.py
import os

class Config:
    """Base configuration for Gelato Play."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key-here')  # Change this in production
    DEBUG = True  # Set to False in production
    FLASK_ENV = 'development'  # Switch to 'production' later
    TEMPLATES_AUTO_RELOAD = True  # Auto-reload templates during development
