import os
import telegram

from bottle import Bottle, request

app = Bottle()

@app.get('/api')
def api():
    TELEGRAM_TOKEN = os.getenv("telegram_token")
    if not TELEGRAM_TOKEN:
        return {"status": "error", "reason": "no tg token"}
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        chat_id = update.message.chat.id
        # Reply with the same message
        bot.sendMessage(chat_id=chat_id, text=update.message.text)
    return {"status": "ok"}
