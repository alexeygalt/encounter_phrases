from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, FSInputFile
from src.const import PHRASES
from src.lexicon.lexicon import HELP_MESSAGE
from src.utils import search_word_in_phraseological_list, send_long_message

router = Router()


class Form(StatesGroup):
    waiting_for_word = State()


@router.message(CommandStart())
async def process_start_command(message: Message, state: FSMContext):
    await message.answer_photo(photo=FSInputFile("src/static/enc.jpg"))
    await message.answer("Введите слово для поиска. Напишите /stop для завершения.")
    await state.set_state(Form.waiting_for_word)


@router.message(Command(commands='stop'))
async def process_stop_command(message: Message, state: FSMContext):
    await message.answer("Вы завершили поиск. Напишите /start для начала нового поиска.")
    await state.clear()


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(HELP_MESSAGE)


@router.message()
async def handle_search_query(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state == Form.waiting_for_word.state:
        if message.text.startswith('/'):
            return

        user_query = message.text
        search_result = search_word_in_phraseological_list(PHRASES, user_query)

        if search_result:
            response = '\n'.join(search_result)
        else:
            response = "Ничего не найдено."

        await send_long_message(message.answer, response)