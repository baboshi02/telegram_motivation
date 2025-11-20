#!env/bin/python3
import os
import dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import requests

dotenv.load_dotenv()

TELEGRAM_BOT_API_KEY = os.getenv("TELEGRAM_API_KEY")
NINJA_API_KEY = os.getenv("NINJA_API_KEY")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    username = update.effective_sender.username
    if username:
        await context.bot.send_message(
            chat_id=update.effective_chat.id, text=("Hello " + username)
        )

    else:
        await context.bot.send_message(
            chat_id=update.effective_chat.id, text=("Hello person")
        )


async def motivate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        response = requests.get(
            "https://zenquotes.io/api/random",
        )
        quote = response.json()[0]["q"]
        await context.bot.send_message(chat_id=update.effective_chat.id, text=quote)
    except Exception:
        await context.bot.send_message(
            chat_id=update.effective_chat.id, text="Sorry an error occured"
        )


if __name__ == "__main__":
    if not TELEGRAM_BOT_API_KEY:
        raise BaseException("Provide valid Telegram Bot Api Key")
    if not NINJA_API_KEY:
        raise BaseException("Provide valid NINJA api key")
    application = ApplicationBuilder().token(TELEGRAM_BOT_API_KEY).build()
    start_handler = CommandHandler("start", start)
    motivate_handler = CommandHandler("motivate", motivate)
    application.add_handlers([start_handler, motivate_handler])
    application.run_polling()
