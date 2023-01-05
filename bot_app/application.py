
from telegram import Update, Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, MessageHandler, CommandHandler, filters, CallbackContext, CallbackQueryHandler
from . import datahandler

class BotApp:
    def __init__(self, TELEGRAM_TOKEN: str):
        self.TOKEN = TELEGRAM_TOKEN
        self.app = None
        pass
    
    def run(self):
        self.app = Application.builder().token(self.TOKEN).build()
        self.add_handlers()
        self.app.run_polling()
        pass

    def add_handlers(self):
        self.app.add_handler(CommandHandler("start", self.start_handler))
        self.app.add_handler(CallbackQueryHandler(self.button))
        pass

    async def start_handler(self, update: Update, context: CallbackContext):
        with open('./bot_app/resources/greeting.txt','r') as file:
            text = file.read()
        await context.bot.send_message(
            chat_id = update.message.chat_id,
            text = text, 
            parse_mode = 'HTML'
        )
        await self.actions_buttons_handler(update, context)
        pass
    
    async def actions_buttons_handler(self, update: Update, context: CallbackContext):
        keyboard = [
            [InlineKeyboardButton("cryptocurrency prices", callback_data="1")]
        ]
        buttons = InlineKeyboardMarkup(keyboard)
        await context.bot.send_message(
            chat_id = update.message.chat_id,
            text = "Options",
            reply_markup = buttons
        )
        pass

    async def button(self, update: Update, context: CallbackContext):
        """Parses the CallbackQuery and updates the message text."""
        query = update.callback_query
        await query.answer()
        if query.data == '1':
            await self.show_crypto_currencies(query, context)
        pass

    async def show_crypto_currencies(self, query, context):
        data = datahandler._get_crypto_currencies()
        await context.bot.send_message(
            chat_id = query.message.chat_id,
            text = data, 
            parse_mode = 'HTML'
        )
        pass
    pass



