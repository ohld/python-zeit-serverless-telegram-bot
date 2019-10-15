import os
import telegram

from flask import Flask, jsonify, Response, request
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
def catch_all(path):
    return Response("<h1>Flask is working</h1>")

@app.route('/api')
def api():
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
    if not TELEGRAM_TOKEN:
        return jsonify({"status": "error", "reason": "no tg token"})
        
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    print("REQUEST:", str(request))
    print("REQUEST METHOD:", str(request.method))
    print("REQUEST JSON:", str(request.get_json(force=True)))

    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        chat_id = update.message.chat.id
        # Reply with the same message
        bot.sendMessage(chat_id=chat_id, text=update.message.text)
    return jsonify({"status": "ok"})
