import req
#=========================================
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

async def start_func(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.sendMessage(chat_id=update.effective_chat.id, text="َbot is runing ...")

application = ApplicationBuilder().token("8357218914:AAFhG8hF5ZMK3OknROHcNpnkyeuyYrjFmoo").build()

start_handler = CommandHandler('start', start_func)
application.add_handler(start_handler)
#=========================================
#=========================================
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello_world():
    return "<p>Welcome to Telegram bot for describing images!</p>"
app.run(port=7799,host='127.0.0.1')

#=========================================


















# def run_app():
#     app.run(port=7999,host='0.0.0.0')

# t = threading.Thread(target=run_app, args = ())
# t.start()