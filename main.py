from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import handlers

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hola! Soy un bot de tareas. Usa /ayuda para ver los comandos disponibles.')
    logging.info(f"Bot started by {update.effective_user.first_name}.")

def main() -> None:
    try:
        with open("telegram_token.txt", "r") as token_file:
            token = token_file.read().strip()
    except FileNotFoundError as e:
        logging.error(f"Error reading the token file: {e}")
        return

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
        try:
            handlers.save_tasks()
            logging.info("Bot is shutting down and saving tasks.")
        except Exception as e:
            logging.error(f"Error while shutting down: {e}")

    updater.dispatcher.add_error_handler(shutdown)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()