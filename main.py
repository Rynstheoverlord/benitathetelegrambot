from telegram.ext import Application, MessageHandler, CommandHandler, ContextTypes, filters
from telegram import Update
import random, time
import json
import threading
from bot import get_message
from keep_alive import keep_awake
import nltk
nltk.download('punkt')





BOT_TOKEN = "5893981732:AAFGrSHXseIoi_C_YXxGLlPflGTYLot6ixM"
BOT_USERNAME = "@benitathebot"


async def start(update: Update, context: ContextTypes):
  await update.message.reply_text(
    "Hi, nice to meet you, I'm Benita, how do you do?.")


async def help(update: Update, context: ContextTypes):
  await update.message.reply_text(f"""Here are a list of my functions:
  
  /start - Starts the bot
  /help - Displays this message
/ytvideo [url] - To download a youtube video

Sorry that's all for now☺️""")

async def handle_messages(update: Update, context: ContextTypes):
  message = update.message.text
  bot_reply = get_message(message)
  await update.message.reply_text(bot_reply)



def main():
  print("Starting bot...")
  app = Application.builder()
  app = app.token(BOT_TOKEN).build()

  app.add_handler(CommandHandler("start", start))
  app.add_handler(CommandHandler("help", help))

  
  app.add_handler(MessageHandler(filters.TEXT, handle_messages))

  app.run_polling(poll_interval=3)


if __name__ == '__main__':
  keep_awake()
  main()
