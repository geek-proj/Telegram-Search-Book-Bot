try: 
	from googlesearch import search 
	import telebot
except ImportError:  
	print("No module named found") 

class TelegramBot:
	def __init__(self,token):
		self.bot = telebot.TeleBot(token)

	def customSending(self):
		@self.bot.message_handler(commands=['start', 'help'])
		def send_welcome(message):
			self.bot.reply_to(message, "Hi, type your lovely book")

	def customGetText(self):
		@self.bot.message_handler(content_types=['text'])
		def get_text_messages(message):
			numOf = 10
			encode = message.text.encode('utf-8')
			self.bot.send_message(message.from_user.id,'Wait...')
			for j in search("{} pdf".format(encode), tld="co.in", num=numOf, stop=10, pause=2):
				if j.find('pdf') != -1 or j.find('PDF')!=-1:
				  self.bot.send_message(message.from_user.id,j)
				  break

	def poolIt(self):
		self.bot.polling()

telegramBot = TelegramBot('1299770172:AAEujHQbTBRHqspC6Im9dVnuHxg-Gg_0wYs')
telegramBot.customSending()
telegramBot.customGetText()
telegramBot.poolIt()