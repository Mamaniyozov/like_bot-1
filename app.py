from flask import Flask,request
import telegram 
import os 
from telegram import Bot, Update
from telegram.ext import Dispatcher,Updater, CommandHandler, MessageHandler, Filters,CallbackContext,CallbackQueryHandler
from like_bot import(
    start,
    get_image,
    callback_like
)
app = Flask(__name__)

# bot
TOKEN = os.environ['TOKEN']
bot = Bot(token=TOKEN)


@app.route('/', methods=['POST'])
def main():
    print(request.form)
    return 'OK'
@app.route('/add_like', methods=['POST'])
def main():
    if request.method == 'GET':
        return {'status': 200}

    elif request.method == 'POST':
        # get data from request
        data: dict = request.get_json(force=True)

        # convert data to Update obj
        update: Update = Update.de_json(data, bot)

        # Dispatcher
        dp: Dispatcher = Dispatcher(bot, None, workers=0)

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.photo, get_image))
    dp.add_handler(CallbackQueryHandler(callback_like))
    dp.process_update(update=update)
    return {'status': 200}
if __name__ == '__main__':
    app.run(debug=True)