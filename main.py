import psutil
import telebot
bot_token = '5341491111:AAHXyOJmIz-vqcSz0jreWcD9nXOek0pT8AM'
chat_id = '1829352344'
bot = telebot.TeleBot(bot_token)
message_list = []
with open('message.txt', 'r', encoding='utf-8') as f:
	for line in f:
		message = [int(line.strip().split('|')[0]), line.strip().split('|')[1], True]
		if message not in message_list:
			message_list.append(message)
while True:
	battery = psutil.sensors_battery()
	percent = int(battery.percent)

	for message in message_list:
		if percent == message[0] and message[2] == True:
			bot.send_message(chat_id, f'{message[1]}')
			message[2] = False
bot.infinity_polling()