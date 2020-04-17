import os
import logging
import telegram

from flask import Flask, jsonify, Response, request
app = Flask(__name__)


def generate_cats():
    import random
    
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
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    return jsonify(bot.get_me())
    

@app.route('/api', methods=['GET', 'POST'])
def api():
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
    if not TELEGRAM_TOKEN:
        return jsonify({"status": "error", "reason": "no tg token"})
        
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    
    print(bot.get_me())

    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        chat_id = update.message.chat.id
        # Reply with the same message
        text = generate_cats() # update.message.text
        bot.sendMessage(chat_id=chat_id, text=text)
        
    return jsonify({"status": "ok"})
