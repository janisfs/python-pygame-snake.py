   import telebot


   # Замените 'YOUR_API_TOKEN' на токен вашего бота
   API_TOKEN = '6155498030:AAF7j1BU7ao-Nbw0OqmkfRR2CaP5qwvbw0I'
   bot = telebot.TeleBot(API_TOKEN)

   @bot.message_handler(func=lambda message: True)  # Обрабатываем все сообщения
   def echo_all(message):
       bot.reply_to(message, "Привет, этот бот лежит на локальном сервере с автозапуском!")

   if __name__ == '__main__':
       print("Бот запущен...")
       bot.polling(none_stop=True)  # Запуск бота


   # Запускаем бота
   # Замените 'YOUR_API_TOKEN' на токен вашего бота
   python bot.py