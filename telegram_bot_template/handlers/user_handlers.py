from aiogram import Router
from aiogram.filters import CommandStart, Command, Text
from aiogram.types import Message
from keyboards.keyboards import game_kb, yes_no_kb
from lexicon.lexicon_ru import LEXICON_RU
from services.services import get_bot_choice, get_winner

router: Router = Router()

@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=yes_no_kb)

@router.message(Command(commands='/help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'], reply_markup=yes_no_kb)

