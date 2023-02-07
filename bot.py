from aiogram import Bot, Dispatcher,executor, types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pytube import YouTube
import logging

logging.basicConfig(level= logging.INFO)

TOKEN = '5716676902:AAFt3xSuQSRg4YjUiHGcKstbzU9fMCDphWc'
bot = Bot(token = TOKEN)
dp = Dispatcher(bot)
video_url = ''

@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    await message.reply('Hello! i`m botie_bot')

@dp.message_handler(commands = ['find'])
async def find_video(message: types.Message):
    button1 = InlineKeyboardButton(text='download', callback_data='download')
    keyboard_inline = InlineKeyboardMarkup().add(button1)
    video_url = message.text.split()[1]
    print(video_url)
    await message.reply('downloading', reply_markup=keyboard_inline)

@dp.callback_query_handler(text = ['download'])
async def send_video(call: types.CallbackQuery):
    print(logging.info(video_url))
    yt = YouTube (video_url)
    stream = yt.streams.get_highest_resolution ()
    stream.download (f'YoutubeDownload/')
    await call.message.answer_video(video = open(f'YoutubeDownload/{stream.default_filename}', "rb"))



"""@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)"""

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)