import logging
from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv # To load the secret from .env 
import os
import asyncio

load_dotenv()   # This function automatically detect .env file.
API_TOKEN=os.getenv("TOKEN")
# print(API_TOKEN)

# Logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher

bot = Bot(token=API_TOKEN)
dp= Dispatcher(bot) # It help to make conncetion with telegram bot.

@dp.message_handler(commands=['start','help'])
async def command_start_handler(message: types.Message):
    """
    This handler revives message with '/start' command
    """
    await message.reply(f"hello \n I am Echo Bot! \n powered by abishek.")

@dp.message_handler()
async def echo(message: types.Message):
    """
    This will return echo
    """
    await message.answer(message.text)





if __name__ == "__main__":
    from aiogram import executor
    # asyncio.run(main())
    executor.start_polling(dp, skip_updates=True)


