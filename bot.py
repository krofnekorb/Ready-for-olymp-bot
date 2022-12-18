import telebot

from constants import token
from interface_provider import main_menu_markup, task_menu_markup
from tasks_and_solutions_loader import load_solution, load_task
from user import User
from language_mapper import from_russian_to_english_mapping_holder, map_from_russian_to_english

# инициализируем бота
bot = telebot.TeleBot(token)

# инициализируем словарь, в котором будем хранить юзеров
# в качестве ключей словаря используются chat_id, в качестве значений - объекты класса User
users_info_holder = dict()


# создает юзера и кладет его в словарь users_info_holder
def on_user_init(message):
    user = User(message.from_user.username)
    users_info_holder[message.chat.id] = user
    return user


# функция для апдейта прогресса юзеров и сброса текущей секции
def update_user_progress_and_reset_section(chat_id):
    user = users_info_holder.get(chat_id)
    user.update_progress()
    user.reset_current_section()


# регистрирует юзера
@bot.message_handler(commands=['start'])
def start(message):
    user = on_user_init(message)
    bot.send_message(
        message.chat.id,
        text='Привет, {}, я бот для подготовки к олимпиаде, выбери тему задачи'.format(
            user.get_username()
        ),
        reply_markup=main_menu_markup
    )


@bot.message_handler(content_types=['text'])
def ask_for_task(message):
    stripped_message = message.text.strip()
    chat_id = message.chat.id
    user = users_info_holder.get(chat_id)
    if user is None:
        bot.send_message(chat_id, 'Напиши /start для инициализации бота')
        return
    if stripped_message in from_russian_to_english_mapping_holder.keys():
        current_section_in_en = map_from_russian_to_english(stripped_message)
        user.set_current_section(current_section_in_en)
        problems = load_task(current_section_in_en, user.get_current_task_number())
        if problems == '':
            bot.send_message(chat_id, 'Ты решил АБСОЛЮТНО всё!')
            return
        bot.send_photo(chat_id, photo=problems)
        bot.send_message(chat_id, text='Что дальше?', reply_markup=task_menu_markup)
    if stripped_message == 'Посмотреть решение':
        solution = load_solution(user.get_current_section(), user.get_current_task_number())
        bot.send_photo(chat_id, photo=solution)
    elif stripped_message == 'Еще задачу!':
        update_user_progress_and_reset_section(chat_id)
        bot.send_message(chat_id, text='Выбери раздел'.format(message.from_user), reply_markup=main_menu_markup)


bot.infinity_polling()
