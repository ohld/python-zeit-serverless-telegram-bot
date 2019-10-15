# python-zeit-serverless-telegram-bot
Example of Python Serverless Telegram bot to be used with Zeit.co (Now.sh)


## Zeit Serverless
https://dev.to/jolvera/deploy-a-python-serverless-function-on-zeit-now-22cf

## Telegram Serverless
https://seminar.io/2018/09/03/building-serverless-telegram-bot/

## Register webhook
``` bash
curl "https://api.telegram.org/bot<TELEGRAM_TOKEN>/setWebhook?url=https://us-central1-<PROJECT-NAME>.cloudfunctions.net/webhook"
```

curl "https://api.telegram.org/bot835520379:AAHNEMSwOgTHI5d8PdTJUY1ujW4D-DN89w8/setWebhook?url=https://python-zeit-serverless-telegram-bot.okhlopkov.now.sh/api"