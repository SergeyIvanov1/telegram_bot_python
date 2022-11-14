from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import game
from  bot_commands import *



app = ApplicationBuilder().token("5781661768:AAHuLtsRFbq5h5NsCHZTHxGmZ1-veS_52f0").build()
print('server started')

app.add_handler(CommandHandler("hello", hello_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("game", game_command))
app.add_handler(CommandHandler("input", input_command))
app.add_handler(CommandHandler("result", result_command))
app.run_polling()