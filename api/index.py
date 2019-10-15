import os
import telegram

from bottle import Bottle, request

app = Bottle()

@app.get('/api')
def api():
    bot = telegram.Bot(token=os.environ["telegram_token"])
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        chat_id = update.message.chat.id
        # Reply with the same message
        bot.sendMessage(chat_id=chat_id, text=update.message.text)
    return "ok"
