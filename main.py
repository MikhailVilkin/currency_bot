from config import bot_config as cfg
import bot_app as app

    
def main():
    bot = app.BotApp(cfg.BOT_TOKEN)
    bot.run()


if __name__ == "__main__":
    main()
