# Configuration file for backend settings

import os

class Config:
    """Base configuration"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    
    # Flask settings
    DEBUG = True
    TESTING = False
    
    # File paths
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_DIR = os.path.join(BASE_DIR, 'data')
    HTML_FILE = os.path.join(BASE_DIR, '..', 'index.html')
    
    # Git settings
    GIT_BRANCH = os.environ.get('GIT_BRANCH') or 'main'
    AUTO_PUSH = os.environ.get('AUTO_PUSH', 'False').lower() == 'true'
    
    # CORS settings
    CORS_ORIGINS = ['http://localhost:5000', 'http://127.0.0.1:5000']
    
    # JSON file paths
    REVIEWS_FILE = os.path.join(DATA_DIR, 'reviews.json')
    FAQS_FILE = os.path.join(DATA_DIR, 'faqs.json')
    GALLERY_FILE = os.path.join(DATA_DIR, 'gallery.json')
    REELS_FILE = os.path.join(DATA_DIR, 'reels.json')

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    TESTING = False

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY')  # Must be set in production
    
    # Production CORS settings
    CORS_ORIGINS = os.environ.get('CORS_ORIGINS', '').split(',')

class TestingConfig(Config):
    """Testing configuration"""
    DEBUG = True
    TESTING = True

# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
