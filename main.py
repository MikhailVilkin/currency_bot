from config import bot_config as cfg
import bot_app as app

# async def do_echo(update: Update, context: CallbackContext):
#     reply_message = 'hi'
    
#     bot = context.bot
#     await bot.send_message(
#             chat_id = update.message.chat_id,
#             reply_to_message_id = update.message.message_id,
#             text=reply_message,
#         )


# def main():
#     app = Application.builder().token(cfg.BOT_TOKEN).build()
#     message_handler = MessageHandler(filters.Text(), do_echo)
#     app.add_handler(message_handler)
#     app.run_polling()
    
def main():
    bot = app.BotApp(cfg.BOT_TOKEN)
    bot.run()


if __name__ == "__main__":
    main()
