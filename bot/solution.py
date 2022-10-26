from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *
import json

def get_token():
    with open('token.json', 'r', encoding='utf-8') as f: 
        token = json.load(f) 
        return token 

app = ApplicationBuilder().token(get_token()["token"]).build()
print("server started")

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))

app.add_handler(CommandHandler("ratio_calculator", ratio_calculator_command))
app.add_handler(CommandHandler("racio_sum", culc_command)) 
app.add_handler(CommandHandler("racio_sub", culc_command)) 
app.add_handler(CommandHandler("racio_mult", culc_command)) 
app.add_handler(CommandHandler("racio_div", culc_command)) 

app.add_handler(CommandHandler("complex_calculator", complex_calculator_command))
app.add_handler(CommandHandler("complex_sum", complex_command)) 
app.add_handler(CommandHandler("complex_sub", complex_command)) 
app.add_handler(CommandHandler("complex_mult", complex_command)) 
app.add_handler(CommandHandler("complex_div", complex_command)) 

app.add_handler(CommandHandler("phone_dictionary", phone_dictionary_command))
app.add_handler(CommandHandler("input", input_command)) 
app.add_handler(CommandHandler("data", data_command))
app.add_handler(CommandHandler("get", get_command)) 

app.run_polling()