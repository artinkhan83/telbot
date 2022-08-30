import api as C
from telegram.ext import *
from telegram import Update
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime
import jdatetime

print('xmain is runed...')

def main():
    updater = Updater(C.API_BOT, use_context=1)
    dp=updater.dispatcher
    dp.add_handler(CommandHandler("start",start))
    dp.add_handler(MessageHandler(Filters.text,hanmsg))
    dp.add_handler(CallbackQueryHandler(callBackQuery))
    
    updater.start_polling()
    updater.idle()
    
def start(update, context):
    markup = InlineKeyboardMarkup(
        [[InlineKeyboardButton('ALIREZA', callback_data='alirzw')]])
     
    update.message.reply_text('@Telfixe',reply_markup=markup)
    
def callBackQuery(update: Update, context: CallbackContext): 
    data = update.callback_query.data
    if data == 'alirzw':
        update.callback_query.answer('Creator')
    elif data == 'time':
        update.callback_query.answer(date())
def time():
    today = datetime.now()
    time = today.strftime('%H:%M:%S')
    markup = InlineKeyboardMarkup(
        [[InlineKeyboardButton(time, callback_data='time')]])
    return markup

def date():
    today = jdatetime.date.today()
    tarikh = today.strftime('%Y/%m/%d')
    return tarikh

def hanmsg(update, context):
    text = update.message.text
    text=str(text).lower()
    if text == 'time':
        update.message.reply_text('Time is:', reply_markup=time())
    
main()
