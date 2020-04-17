import os
import random
import logging
import telegram

from flask import Flask, jsonify, Response, request
app = Flask(__name__)


def generate_cats():    
    cs_all = [
        "👊 Опасность",
        "💪 Брутальность",
        "⭐️ Заметность",
        "⚡️ Актуальность",
        "😍 Сексуальность",
        "😱 Неординарность",
        "🤙 Прошаренность",
        "♻️ Экологичность",
    ]
    
    cs = random.sample(cs_all, 3)
    
    t = f"""
{c[0]}: {random.randint(4,6)}/5
{c[1]}: {random.randint(3,6)}/5
{c[2]}: {random.randint(1,6)}/5
    """
        
    return t
        
    
@app.route('/', methods=['GET'])
def getme():
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
    bot = telegram.Bot(TELEGRAM_TOKEN)
    return str(bot.get_me())
    

@app.route('/api', methods=['GET', 'POST'])
def api():
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
    if TELEGRAM_TOKEN is None:
        return jsonify({"status": "error", "reason": "no tg token"})
        
    bot = telegram.Bot(TELEGRAM_TOKEN)
    
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        chat_id = update.message.chat.id
        # Reply with the same message
        text = update.message.text  # generate_cats() 
        bot.sendMessage(chat_id=chat_id, text=text)
    else:
        return str(bot.get_me())
        
    return jsonify({"status": "ok"})
