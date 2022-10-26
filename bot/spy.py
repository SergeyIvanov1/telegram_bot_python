from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackContext
import datetime
import codecs

# ContextTypes.DEFAULT_TYPE
def log(update: Update, context: CallbackContext):
    file = codecs.open('db.csv', 'a', 'utf-8')
    file.write(f'[{datetime.datetime.now()}] first_name = {update.effective_user.first_name}, id = {update.effective_user.id}, request = {update.message.text}\n')
    file.close()