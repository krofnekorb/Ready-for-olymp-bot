from telebot import types

main_menu_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('ТФКП')
btn2 = types.KeyboardButton('Линейная алгебра')
btn3 = types.KeyboardButton('Классический анализ')
btn4 = types.KeyboardButton('Алгебра')
btn5 = types.KeyboardButton('Комбинаторика')
btn6 = types.KeyboardButton('Теория вероятностей')
main_menu_markup.add(btn1, btn2, btn3, btn4, btn5, btn6)

task_menu_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('Посмотреть решение')
btn2 = types.KeyboardButton('Еще задачу!')
task_menu_markup.add(btn1, btn2)
