from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from spy import *
import calculator
import phone_dictionary
import logger

async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    await update.message.reply_text(f'Hi {update.effective_user.first_name}!')


async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'{datetime.datetime.now().time()}')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'menu\n/hi\n/time\n/help\n/ratio_calculator\n/complex_calculator\n/phone_dictionary')

async def ratio_calculator_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'ratio numbers calculator\n/racio_sum\n/racio_sub\n/racio_mult\n/racio_div')

async def complex_calculator_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'complex numbers calculator\n/complex_sum\n/complex_sub\n/complex_mult\n/complex_div') 

async def phone_dictionary_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'choose command: \n1. input data to file or get data from file \n2. and specify path\n/input\n/get') 
# /data Sapognikov Alexey Mikhailovich driver 1

async def input_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text('Input command - data \nand: last_name first_name patronymic description format (1. Vertical OR 2. Horizontal)') 
    
async def data_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    logger.info('query = ' + msg)
    items = msg.split()
    data = []
    last_name = items[1]
    first_name = items[2]
    patronymic = items[3]
    description = items[4]
    data.append(last_name)
    data.append(first_name)
    data.append(patronymic)
    data.append(description)
    format = int(items[5])
    phone_dictionary.write_data_to_file(data, format)
    # await update.message.reply_text(calculator.racio_sum(x, y)) 

# /data Петров Сидр Иванович водитель 1
# /get format1.txt

async def get_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    path = items[1]
    string = phone_dictionary.outputing_all_data(path)
    await update.message.reply_text(string)     
    

async def culc_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split(' ')
    x = int(items[1])
    y = int(items[2])

    command = items[0]
    match command:
        case '/racio_sum':
            method = calculator.racio_sum
        case '/racio_sub':
            method = calculator.racio_sub
        case '/racio_mult':
            method = calculator.racio_mult
        case '/racio_div':
            method = calculator.racio_div
    await update.message.reply_text(method(x, y))  

async def complex_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split(',')
    
    x = items[1]
    y = items[2]

    command = items[0]
    await update.message.reply_text(calculator.complex_method(command, x, y))  

    # /complex_sum 3 + 0i 1 + 5i
# C:\Users\User\Desktop\Programing\python\seminar9\bot