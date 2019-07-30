from telegram.ext import Updater

from bot.test_controller import TestController

if __name__ == '__main__':
    updater = Updater(token="491561648:d6506e5fcfa7a3804bba78d528445392965f2de5")
    dispatcher = updater.dispatcher
    test_controller = TestController(dispatcher=dispatcher)
    updater.start_polling(poll_interval=1)
    updater.idle()
