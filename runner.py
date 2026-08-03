import subprocess
import sys
from threading import Thread
from flask import Flask
from loguru import logger

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is alive"

def run_flask():
    app.run(host='0.0.0.0', port=8080)

def run_bot():
    while True:
        try:
            logger.info("Bot Starting...")
            subprocess.run([sys.executable, "ayyan_private_hosting.py"])
        except Exception as e:
            logger.error(f"Bot crashed: {e}")

if __name__ == "__main__":
    Thread(target=run_flask).start()
    run_bot()