from telegram import Update, ParseMode
from telegram.ext import CallbackContext
import datetime
import utils

tasks = []

def add_task(update: Update, context: CallbackContext) -> None:
    if len(context.args) < 2:
        update.message.reply_text('Uso incorrecto. Ejemplo: /agregar "Tarea" "YYYY-MM-DD HH:MM"')
        return

    task_description = ' '.join(context.args[:-1])
    try:
        reminder_time = datetime.datetime.strptime(context.args[-1], "%Y-%m-%d %H:%M")
    except ValueError:
        update.message.reply_text('Formato de fecha incorrecto. Use YYYY-MM-DD HH:MM.')
        return

    task = {
        'description': task_description,
        'reminder': reminder_time
    }
    tasks.append(task)
    update.message.reply_text(f'Tarea agregada: "{task_description}" con recordatorio para {utils.format_date(reminder_time)}')

def list_tasks(update: Update, context: CallbackContext) -> None:
    if not tasks:
        update.message.reply_text('No hay tareas en la lista.')
        return

    task_list = "\n".join([f"{i+1}. {task['description']} - Recordatorio: {utils.format_date(task['reminder'])}" for i, task in enumerate(tasks)])
    update.message.reply_text(f'Tareas pendientes:\n{task_list}', parse_mode=ParseMode.MARKDOWN)

def delete_task(update: Update, context: CallbackContext) -> None:
    if len(context.args) < 1:
        update.message.reply_text('Uso incorrecto. Ejemplo: /eliminar 1')
        return

    try:
        task_index = int(context.args[0]) - 1
        if 0 <= task_index < len(tasks):
            deleted_task = tasks.pop(task_index)
            update.message.reply_text(f'Tarea eliminada: "{deleted_task["description"]}" con recordatorio para {utils.format_date(deleted_task["reminder"])}')
        else:
            update.message.reply_text('Índice de tarea no válido.')
    except ValueError:
        update.message.reply_text('El índice debe ser un número.')

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Comandos disponibles:\n/start - Iniciar el bot\n/ayuda - Ver comandos disponibles\n/agregar "Tarea" "YYYY-MM-DD HH:MM" - Agregar una tarea con recordatorio\n/listar - Listar todas las tareas\n/eliminar <índice> - Eliminar una tarea por índice')