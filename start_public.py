#!/usr/bin/env python3
"""
Запуск приложения с публичным доступом через ngrok
"""
import os
import sys
import threading
import asyncio
import logging
from pyngrok import ngrok

# Добавляем путь к приложению
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'edprog'))

from edprog.app import app, Config
from edprog.bot import bot, dp

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("PublicRunner")

def setup_ngrok():
    """Настройка и запуск ngrok туннеля"""
    try:
        # Открываем туннель для Flask приложения
        public_url = ngrok.connect(Config.FLASK_PORT)
        logger.info(f"🌐 ngrok туннель установлен: {public_url}")
        
        # Сохраняем URL в переменную окружения для конфига
        public_url_str = str(public_url)
        if public_url_str.startswith('NgrokTunnel'):
            public_url_str = public_url_str.split('->')[0].strip()
        
        os.environ['WEB_APP_URL'] = public_url_str + '/auth_start.html'
        logger.info(f"✅ WEB_APP_URL установлен: {os.environ['WEB_APP_URL']}")
        
        return public_url_str
    except Exception as e:
        logger.warning(f"⚠️  ngrok недоступен ({type(e).__name__})")
        logger.warning(f"   Используется стандартный публичный URL: {Config.WEB_APP_URL}")
        logger.info("   💡 Для использования ngrok: https://dashboard.ngrok.com/get-started/your-authtoken")
        return None

def run_flask():
    """Запуск Flask приложения"""
    logger.info(f"🚀 Flask запускается на http://{Config.FLASK_HOST}:{Config.FLASK_PORT}")
    app.run(host=Config.FLASK_HOST, port=Config.FLASK_PORT, debug=Config.FLASK_DEBUG, use_reloader=False)

async def run_bot():
    """Запуск Telegram бота"""
    logger.info(f"🤖 Telegram бот запускается (TOKEN: {Config.BOT_TOKEN[:20]}...)")
    logger.info(f"📱 Web App URL: {os.environ.get('WEB_APP_URL', Config.WEB_APP_URL)}")
    await dp.start_polling(bot)

def run_bot_sync():
    """Синхронный запуск бота"""
    asyncio.run(run_bot())

if __name__ == '__main__':
    logger.info("=" * 60)
    logger.info("🎯 Запуск Telegram Web App + Бот (ПУБЛИЧНЫЙ РЕЖИМ)")
    logger.info("=" * 60)
    
    # Устанавливаем ngrok туннель
    public_url = setup_ngrok()
    
    # Запускаем Flask в отдельном потоке
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()
    logger.info(f"✅ Flask запущен на http://{Config.FLASK_HOST}:{Config.FLASK_PORT}")
    
    # Запускаем бота в главном потоке
    try:
        run_bot_sync()
    except KeyboardInterrupt:
        logger.info("⏹️  Остановка приложения...")
        ngrok.kill()
