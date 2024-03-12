from dotenv import load_dotenv
import os
from aiogram import Bot, Dispatcher, executor, types
import openai
import sys

class Reference: 
    '''
    A class to store previously responce from the chatGPT API.
    '''
    def __init__(self)->None:
        self.response= ""

load_dotenv()
openai.api_key=os.getenv("OpenAI_API_KEY")

reference=Reference()

TOKEN= os.getenv("TOKEN") # Bot token

#Openai model name
MODEL_NAME= "gpt-3.5-turbo"

# Initialize bot and dispatcher
bot = Bot(token=TOKEN)
dp= Dispatcher(bot)

def clear_post():
    """
    A function to clear the previous conversation and context.
    """
    reference.response= ""


@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    """
    This handler revives message with '/start' command
    """
    await message.reply(f"hello \n I am Tele Bot! \n powered by abishek.\n how can i assist you ?")

# Function to clear the previous context.
@dp.message_handler(commands=['clear'])
async def clear(message: types.Message):
    """
    A handler to clear the previous conversation and context.
    """
    clear_post()
    await message.reply("I've cleared the past conversaion and context")

@dp.message_handler(commands=['help'])
async def helper(message: types.Message):
    """
    A handler to display the help menu.
    """
    help_command= """ Hi there, I'm chatGPT Telegram bot created by Abishek ! Please follow these commands
     /start - to start conversation
     /clear - to clear the past conversation and context.
     /help - to get this help menu.
     I help this helps :)
    """
    await message.reply(help_command)



# OpenAi 
@dp.message_handler()
async def chatgpt(message: types.Message):
    """
    A handler to process the users input and generate a responce using the chatGPT API
    """
    print(f">>> user: \n\t{message.text}")
    

    response = openai.chat.completions.create(
    model=MODEL_NAME,
    messages=[
        {"role": "assistant", "content": reference.response}, # role of assistant
        {"role": "user", "content": message.text}, # our query
        ])
    reference.response = response['choices'][0]['message']['content']
    print(f">>>> chatGPT: \n\t {reference.response}")
    await bot.send_message(chat_id=message.chat.id, text=reference.response)




if __name__ == "__main__":
    from aiogram import executor
    # asyncio.run(main())
    executor.start_polling(dp, skip_updates=True)

