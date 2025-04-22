# Импортируем нужные библиотеки для проекта
import telebot
import requests
import json

# Вводим Токен для дальнейшей работы с телеграм-ботом
TOKEN = "7737702051:AAFWt_2pJTVys6DIZRmQcIJoY6WpeRCGnD0"
bot = telebot.TeleBot(TOKEN)

# Словарь всех доступных валют в данном боте
keys = {
    "биткоин": "BTC",
    "эфириум": "ETH",
    "рипл": "XRP",
    "лайткоин": "LTC",
    "кардано": "ADA",
    "солана": "SOL",
    "доллар": "USD",
    "евро": "EUR",
    "фунт": "GBP",
    "иена": "JPY",
    "франк": "CHF",
    "рубль": "RUB"
}

# Вводим функцию, которая при написании нужных команд пишет приветственное письмо и пример работы
@bot.message_handler(commands=['start', 'help'])
def welcome_command(message):
    text = "Вас приветствует бот: BROTHER_42_FOUNDATION.\n\nДоступные команды:\n/start\n/help\n/values\n\nПример ввода для перевода:\n<НАЧАЛЬНАЯ ВАЛЮТА> <КОНЕЧНАЯ ВАЛЮТА> <КОЛИЧЕСТВО>\n"
    bot.reply_to(message, text)

# Ввводим функцию, которая при написании нужной команды выводит доступные валюты
@bot.message_handler(commands=['values'])
def all_values(message):
    values_text = "Доступные валюты:\n".upper()

    for name, code in keys.items():
        values_text += f"{name} - {code}\n"
    bot.reply_to(message, values_text)

# Вводим функцию, которая разделяет сообщения на нужные данные и в дальнейшем работает с ними.
# Отправляет запрос на сервер, чтобы получить данные о валюте, которую запросил пользователь, в реальном времени.
# После отправяляет обратно нам, где уже мы перемножаем это значение на введённое количество.
# И в финальном этапе выводит пользователю готовое подсчитанное значение.
@bot.message_handler(content_types=['text'])
def cut_message(message):
    x = message.text.split(" ")

    if len(x) < 3:
        bot.reply_to(message,
                     "Данное сообщение содержит меньше нужного количества значений\nТребуемое количество значений - 3")
        return
    elif len(x) > 3:
        bot.reply_to(message,
                     "Данное сообщение содержит больше нужного количества значений\nТребуемое количество значений - 3")
        return

    cur_start, cur_end, amount = x
    cur_start = cur_start.lower()
    cur_end = cur_end.lower()

    try:
        amount = float(amount)
    except ValueError:
        bot.reply_to(message, f"'{amount}' - неверный формат количества. Введите число.")
        return

    if amount <= 0:
        bot.reply_to(message, "Количество валюты должно быть положительным числом")
        return
    elif cur_start not in keys:
        bot.reply_to(message, f"'{cur_start}' - данной валюты не найдено")
        return
    elif cur_end not in keys:
        bot.reply_to(message, f"'{cur_end}' - данной валюты не найдено")
        return

    # Сама логика API, в которой мы берём с сайта значение курса валют
    response = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={keys[cur_start]}&tsyms={keys[cur_end]}")
    result = response.json()
    rate = result[keys[cur_end]] * amount
    text_1 = f"Сумма {amount} {cur_start} в {cur_end} - {rate}"
    bot.reply_to(message, text_1)

# Бот работает продолжает работу даже при ошибках и тп.
bot.polling(none_stop=True)