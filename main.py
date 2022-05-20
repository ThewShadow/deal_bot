import time
import telebot
import flask
import bitrix24 as b24
import socket
import time

local_ip = socket.gethostbyname(socket.gethostname())

token = '5237614948:AAF1sfGVhikBmAb9BeN_2YeQj-n2akZjDBA'
webhook_url = f'https://167.71.78.210:8443/bots/helper/{token}'
bot = telebot.TeleBot(token)



app = flask.Flask(__name__)

@app.route(f'/bots/helper/{token}', methods=['POST'])
def webhook_handler():
    json_data = flask.request.get_data().decode('utf-8')
    bot.process_new_updates([telebot.types.Update.de_json(json_data)])
    return ''


@bot.message_handler(commands=['start'])
def start(message):
    pass	
    bot.send_message(message.chat.id, 'work')

for i in range(3):
    try:
        bot.delete_webhook()
        time.sleep(1.5)
        bot.set_webhook(webhook_url, certificate=open('webhook.crt', 'r'), max_connections=5)
        break
    except:
        continue

application = app

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
