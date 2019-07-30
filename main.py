from telegram.ext import Updater

from bot.test_controller import TestController

if __name__ == '__main__':
    updater = Updater(token="YOUR_BOT_TOKEN")
    dispatcher = updater.dispatcher
    test_controller = TestController(dispatcher=dispatcher)
    updater.start_polling(poll_interval=1)
    updater.idle()
