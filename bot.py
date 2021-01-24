import os
import logging
import pandas as pd

import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

from generate_plot import generate_circle_plot
from etl import ETL
from settings import BOT_TOKEN, SERVER_URL, PORT

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


updater = Updater(token=BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hola! Mandame el excel \"Portfolio.xslx\" y generaré una imagen de tu cartera (de momento nada más)")


def process_file(update, context):
    print("Archivo recibido, generando imagen...")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Archivo recibido, generando imagen...")
    __excel_file = update.message.document.get_file().download()
    df = pd.read_excel(__excel_file)
    df = ETL.preprocess_data(df)

    __figure_path = './figure.png'
    generate_circle_plot(df, __figure_path)

    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(__figure_path, 'rb'))
    print("Imagen enviada")

    os.remove(__excel_file)
    os.remove(__figure_path)


start_handler = CommandHandler('start', start)
excel_handler = MessageHandler(Filters.document, process_file)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(excel_handler)
#
# bot = telegram.Bot(token=BOT_TOKEN)
# bot.setWebhook(SERVER_URL + BOT_TOKEN)

updater.start_polling()
#
# updater.start_webhook(listen="0.0.0.0",
                      # port=PORT,
                      # url_path=BOT_TOKEN)
# updater.bot.setWebhook(SERVER_URL + BOT_TOKEN)
# updater.idle()

