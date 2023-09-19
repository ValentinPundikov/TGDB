from aiogram.filters.command import Command
from aiogram.filters import CommandObject
import logging
import asyncio
from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage.memory import MemoryStorage
from sql_req import *

storage = MemoryStorage()

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="", parse_mode="HTML")
# Диспетчер
dp = Dispatcher()


class Form(StatesGroup):
    name = State()
    age = State()
    number = State()

class Change_data(StatesGroup):
    change_name = State()
    change_age = State()
    change_number = State()

@dp.message(Command("start"))
async def cmd_name(message: types.Message, command: CommandObject,state: FSMContext) -> None:
    infoid = check_id(message.from_user.id)
    if str(infoid) != str(message.from_user.id):
        await state.set_state(Form.name)
        await message.answer("Пожалуйста, зарегистрируйтесь!\nВведите имя:")
        set_id(message.from_user.id)
    else:
        kb = [
            [types.KeyboardButton(text="Информация")],
            [types.KeyboardButton(text="Изменить информацию")]
        ]
        keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
        await message.answer(f"Привет, <b>{str(get_user(message.from_user.id))}</b>", reply_markup=keyboard)


@dp.message(Form.name)
async def process_name(message: types.Message, state: FSMContext) -> None:
    await state.update_data(name=message.text)
    name_for_db = message.text
    add_user(name_for_db, message.from_user.id)
    await state.set_state(Form.age)
    await message.answer("Введите возраст:")

@dp.message(Form.age)
async def process_name(message: types.Message, state: FSMContext) -> None:
    await state.update_data(age=message.text)
    age_for_db = message.text
    add_age(message.from_user.id, age_for_db)
    await state.set_state(Form.number)
    await message.answer("Введите число:")

@dp.message(Form.number)
async def process_name(message: types.Message, state: FSMContext) -> None:
    await state.update_data(number=message.text)
    number_for_db = message.text
    add_number(message.from_user.id, number_for_db)
    kb = [
        [types.KeyboardButton(text="Информация")],
        [types.KeyboardButton(text="Изменить информацию")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer(f"Привет, <b>{str(get_user(message.from_user.id))}</b>", reply_markup=keyboard)




@dp.message(F.text == "Информация")
async def get_info(message: types.Message):
    name = get_user(id)
    age = get_age(id)
    number = get_number(id)
    kb = [
        [types.KeyboardButton(text="Информация")],
        [types.KeyboardButton(text="Изменить информацию")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer(f"Привет!\nТвое имя: <b>{name}</b>\nТвой возраст: <b>{age}</b>\nТвое число: <b>{number}</b>", reply_markup=keyboard)

@dp.message(F.text == "Изменить информацию")
async def change_info(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Изменить имя")],
        [types.KeyboardButton(text="Изменить возраст")],
        [types.KeyboardButton(text="Изменить номер")],
        [types.KeyboardButton(text="Назад")]

    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer(f"Выберите, что хотите изменить", reply_markup=keyboard)




@dp.message(F.text == "Изменить имя")
async def change_name(message: types.Message, state: FSMContext) -> None:
    await state.set_state(Change_data.change_name)
    await message.answer(f"Введите новое имя:")

@dp.message(F.text == "Изменить возраст")
async def change_name(message: types.Message, state: FSMContext) -> None:
    await state.set_state(Change_data.change_age)
    await message.answer(f"Введите новый возраст:")

@dp.message(F.text == "Изменить номер")
async def change_name(message: types.Message, state: FSMContext) -> None:
    await state.set_state(Change_data.change_number)
    await message.answer(f"Введите новый возраст:")

@dp.message(F.text == "Назад")
async def back(message: types.Message) -> None:
    name = get_user(message.from_user.id)
    age = get_age(message.from_user.id)
    number = get_number(message.from_user.id)
    kb = [
        [types.KeyboardButton(text="Информация")],
        [types.KeyboardButton(text="Изменить информацию")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer(f"Привет!\nТвое имя: <b>{name}</b>\nТвой возраст: <b>{age}</b>\nТвое число: <b>{number}</b>", reply_markup=keyboard)


@dp.message(Change_data.change_number)
async def change_number_FSM(message: types.Message, state: FSMContext) -> None:
    await state.update_data(name=message.text)
    number_for_db = message.text
    set_new_number(number_for_db,message.from_user.id)
    name = get_user(id)
    age = get_age(id)
    number = get_number(id)
    kb = [
        [types.KeyboardButton(text="Информация")],
        [types.KeyboardButton(text="Изменить информацию")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer(f"Привет!\nТвое имя: <b>{name}</b>\nТвой возраст: <b>{age}</b>\nТвое число: <b>{number}</b>", reply_markup=keyboard)

@dp.message(Change_data.change_age)
async def change_age_FSM(message: types.Message, state: FSMContext) -> None:
    await state.update_data(name=message.text)
    age_for_db = message.text
    set_new_age(age_for_db,message.from_user.id)
    name = get_user(id)
    age = get_age(id)
    number = get_number(id)
    kb = [
        [types.KeyboardButton(text="Информация")],
        [types.KeyboardButton(text="Изменить информацию")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer(f"Привет!\nТвое имя: <b>{name}</b>\nТвой возраст: <b>{age}</b>\nТвое число: <b>{number}</b>", reply_markup=keyboard)




@dp.message(Change_data.change_name)
async def change_name_FSM(message: types.Message, state: FSMContext) -> None:
    await state.update_data(name=message.text)
    name_for_db = message.text
    set_new_name(name_for_db,message.from_user.id)
    name = get_user(id)
    age = get_age(id)
    number = get_number(id)
    kb = [
        [types.KeyboardButton(text="Информация")],
        [types.KeyboardButton(text="Изменить информацию")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer(f"Привет!\nТвое имя: <b>{name}</b>\nТвой возраст: <b>{age}</b>\nТвое число: <b>{number}</b>", reply_markup=keyboard)

async def main():
    await dp.start_polling(bot)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    create_database()
    asyncio.run(main())