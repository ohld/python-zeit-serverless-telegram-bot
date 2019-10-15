import os
import telegram

from flask import Flask, Response, request
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
def catch_all(path):
    return Response("<h1>Flask on Now</h1><p>You visited: /%s</p>" % (path), mimetype="text/html")

@app.route('/api')
def api():
    TELEGRAM_TOKEN = os.getenv("telegram_token")
    if not TELEGRAM_TOKEN:
        return Response({"status": "error", "reason": "no tg token"})
        
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        chat_id = update.message.chat.id
        # Reply with the same message
        bot.sendMessage(chat_id=chat_id, text=update.message.text)
    return Response({"status": "ok"})
