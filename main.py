from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import handlers

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hola! Soy un bot de tareas. Usa /ayuda para ver los comandos disponibles.')

def main() -> None:
    with open("telegram_token.txt", "r") as token_file:
        token = token_file.read().strip()

    updater = Updater(token)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("ayuda", handlers.help_command))

    # Add more command handlers here...

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()