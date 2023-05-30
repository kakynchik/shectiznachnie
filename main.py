import telebotimport requests
from telebot import typesfrom bs4 import BeautifulSoup
response1 = requests.get("https://minfin.com.ua/ua/currency/usd/")
if response1.status_code == 200:    soup = BeautifulSoup(response1.text, features = "html.parser")
    for i1 in soup.find('div', {'class': "sc-1x32wa2-9 bKmKjX"}):        i1.extract()
        print(i1, "USD")else:
    print(f"nema pidkluchennya {response1.status_code}")response2 = requests.get("https://minfin.com.ua/ua/currency/eur/")
if response2.status_code == 200:    soup = BeautifulSoup(response2.text, features = "html.parser")
    for i2 in soup.find('div', {'class': "sc-1x32wa2-9 bKmKjX"}):        i2.extract()
        print(i2, "EUR")else:
    print(f"nema pidkluchennya {response2.status_code}")response3 = requests.get("https://minfin.com.ua/ua/currency/pln/")
if response3.status_code == 200:
    soup = BeautifulSoup(response3.text, features = "html.parser")    for i3 in soup.find('div', {'class': "sc-1x32wa2-9 bKmKjX"}):
        i3.extract()        print(i3, "PLN")
else:    print(f"nema pidkluchennya {response3.status_code}")
bot = telebot.TeleBot("6019890674:AAFjeIcbLEKTKmM4qcaMbi3fUn4BPnZLy9s")
@bot.message_handler(commands=['start'])
def start(m, res=False):    markup =types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("kyrs dolara")    item2 = types.KeyboardButton("kyrs evro")
    item3 = types.KeyboardButton("kyrs zlotih")    markup.add(item1)
    markup.add(item2)    markup.add(item3)
    bot.send_message(m.chat.id, "ce konvertor valyut, yaka nada?", reply_markup=markup)
@bot.message_handler(content_types=['text'])def handle_text(message):
    if message.text.strip() == "kyrs dolara":        answer = f"kyrs dolara stanovit {i1}"
    elif message.text.strip() == "kyrs evro":        answer = f"kyrs evro stanovit {i2}"
    elif message.text.strip() == "kyrs zlotih":        answer = f"kyrs zlotih stanovit {i3}"
    bot.send_message(message.chat.id, answer)
bot.polling()