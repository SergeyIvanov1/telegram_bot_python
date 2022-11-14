from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from random import randint

count_sweets = 101
first_player_count = 0
bot_count = 0  
    
choose_first_player = 0
choose_bot = 0

async def hello_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hello {update.effective_user.first_name}!')
    

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'/hello\n/help\n/game\n/input\n/result')

async def input_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text    
    print(msg)    
    items = msg.split()
    x = int(items[1])
    
    global choose_first_player
    choose_first_player = x
    global choose_bot
    choose_bot = randint(1, 28) 

    global first_player_count
    global bot_count
    first_player_count += choose_first_player
    bot_count += choose_bot       
    await update.message.reply_text(f'you choosed = {choose_first_player}, choose_bot = {choose_bot}')  
  

async def game_command(update: Update, context: ContextTypes.DEFAULT_TYPE):  
    global choose_first_player
    choose_first_player = 0
    global choose_bot
    choose_bot = 0
    global first_player_count
    global bot_count
    first_player_count = 0
    bot_count = 0  
    await update.message.reply_text(f'Started new game. All value became zero!')


async def result_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global count_sweets
    global choose_first_player
    global choose_bot

    count_sweets -= choose_first_player
    if count_sweets <= 0:
        print('first player is winner')
        count_sweets = 0
        choose_bot = 0
        choose_first_player = 0  
        await update.message.reply_text(f'winner - {update.effective_user.first_name}!') 
        await update.message.reply_text(f'count_sweets = {count_sweets}\nfirst_player_count = {first_player_count}\nbot_count = {bot_count}')
        return               
        
    count_sweets -= choose_bot 
    if count_sweets <= 0:
        print('bot is winner')
        count_sweets = 0
        choose_bot = 0
        choose_first_player = 0        
        await update.message.reply_text(f'winner - bot!') 
        await update.message.reply_text(f'count_sweets = {count_sweets}\nfirst_player_count = {first_player_count}\nbot_count = {bot_count}') 
        return  
               
    await update.message.reply_text(f'count_sweets = {count_sweets}\nfirst_player_count = {first_player_count}\nbot_count = {bot_count}')   