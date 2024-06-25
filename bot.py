from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Replace 'YOUR_BOT_TOKEN' with your actual bot token from BotFather
TOKEN = '7439666370:AAGfBkiFu7JvVr1OmvWEl3znmucw2BL_tQ8'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! Welcome to the bot. How can I assist you today?')

def main():
    # Create the Updater and pass it your bot's token
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register the /start command handler
    dispatcher.add_handler(CommandHandler("start", start))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()
