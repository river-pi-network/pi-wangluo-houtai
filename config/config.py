import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'supersecretkey'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'
    BANK_API_KEY = os.environ.get('BANK_API_KEY')  # 银行API密钥
    PI_NETWORK_API_KEY = os.environ.get('PI_NETWORK_API_KEY')  # Pi网络API密钥
    PI_NETWORK_BASE_URL = "https://api.minepi.com"  # Pi网络API基础URL
    BANK_BASE_URL = "https://api.bank.com"  # 银行API基础URL
