import os

class Config:
    # --- ДАННЫЕ TELEGRAM (my.telegram.org) ---
    TELEGRAM_API_ID = 32547469           # Твой API_ID
    TELEGRAM_API_HASH = '0dc818f0186f243ce3ca4bc3d5af96e3' # Твой API_HASH

    API_ID = TELEGRAM_API_ID
    API_HASH = TELEGRAM_API_HASH

    # --- ДАННЫЕ БОТА ---
    BOT_TOKEN = '8228106633:AAEVrTo1rKZAzYPHeyWstypU9uQp8vRqTTc'
    ADMIN_ID = 75606383

    # --- НАСТРОЙКИ FLASK ---
    SECRET_KEY = 'не_меняй' 
    
    FLASK_HOST = '0.0.0.0'
    # На Replit используется PORT переменная
    FLASK_PORT = int(os.environ.get('PORT', '3000'))
    FLASK_DEBUG = False
    SESSION_DIR = 'sessions'
    
    # --- ВЕБА ПРИЛОЖЕНИЕ ---
    # Используется ngrok для публичного доступа
    WEB_APP_URL = os.environ.get('WEB_APP_URL', 'https://symmetrical-enigma-jjv77wg5ggr63qr75-3000.app.github.dev/')