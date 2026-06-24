from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import handlers

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hola! Soy un bot de tareas. Usa /ayuda para ver los comandos disponibles.')

def main() -> None:
    with open("telegram_token.txt", "r") as token_file:
        token = token_file.read().strip()

    # Cargar las tareas al iniciar el bot
    handlers.load_tasks()

    updater = Updater(token)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("ayuda", handlers.help_command))
    dispatcher.add_handler(CommandHandler("help", handlers.help_command))
    dispatcher.add_handler(CommandHandler("agregar", handlers.add_task))
    dispatcher.add_handler(CommandHandler("listar", handlers.list_tasks))
    dispatcher.add_handler(CommandHandler("eliminar", handlers.delete_task))

    # Guardar las tareas al terminar el bot
    def shutdown():
        handlers.save_tasks()

    updater.dispatcher.add_error_handler(shutdown)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()