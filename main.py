import openpyxl

workbook = openpyxl.Workbook()
sheet = workbook.active

sheet["A1"] = "name"
sheet["B1"] = "location"
sheet["C1"] = "age"
sheet["A2"] = "bunyod"
sheet["A3"] = "nurbek"
sheet["A4"] = "Damir"
sheet["A5"] = "abduqahhor"
sheet["B2"] = "tashkent"
sheet["B3"] = "tashkent"
sheet["B4"] = "tashkent"
sheet["B5"] = "tashkent"
sheet["C2"] = 16
sheet["C3"] = 16
sheet["C4"] = 16
sheet["C5"] = 16
workbook.save("data.xlsx")

import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters.command import Command
from config import Token

logging.basicConfig(level=logging.INFO)
bot = Bot(token=Token)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("Hello ")
    await message.answer("""<pre><code>"
    Salom
    "</pre></code>""", parse_mode = 'html')
    await message.answer(f"your user id {message.from_user.id}")
    sheet["A1"] = "userid"
    sheet["A2"] = message.from_user.id
    workbook.save("users.xlsx")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
