import telebot
import time


token="1066224484:AAF93zWVnAm2Fvo6kqCAOwYNHHWIrX9NzbU"
bot=telebot.TeleBot(token)
dateneed=float(input("чрз сколько минут запустить программу?"))

periodicity=int(input("с какой периодичностю в сек скидывать слова?"))
@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id,"Скидывай текст")
@bot.message_handler(content_types=['text'])
def help_me(message):
		text=message.text
		text=text.split()
		bot.send_message(message.chat.id,dateneed)
		time.sleep(dateneed*60)
		for i in text:
			bot.send_message (message.chat.id,i)
			time.sleep(periodicity)	
		

bot.polling()
