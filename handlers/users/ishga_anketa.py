

from aiogram import types
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext

from loader import dp
from states.states_vakansiya_uz import PersonalData
from keyboards.inline.menuKeyboards_uz import  menu, informatsiya

@dp.callback_query_handler(text="vakansiya")
async def enter_text(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Qaysi yo'nalish bo'yicha ishlamoqchisiz:")
    await PersonalData.qaysi_sohaga.set()

@dp.message_handler(state=PersonalData.qaysi_sohaga)
async def answer_soha(message: Message, state: FSMContext):
    soha = message.text

    await state.update_data(
        {
            'qaysi_sohaga': soha
        }
    )
    await message.answer("To'liq ism sharifingizni kiriting:")
    await PersonalData.fullname.set()

@dp.message_handler(state=PersonalData.fullname)
async def answer_fullname(message: Message, state: FSMContext):
    fullname = message.text

    await state.update_data(
        {
            'fullname': fullname
        }
    )
    await message.answer("Rezyumeni yuboring:")
    await PersonalData.next()

@dp.message_handler(content_types=types.ContentType.DOCUMENT, state=PersonalData.resume)
async def answer_resume(message: Message, state: FSMContext):
    resume = message.document

    await state.update_data(
        {
            'resume': resume.file_name
        }
    )
    await message.answer("Telefon raqamingizni yuboring:")
    await PersonalData.next()

@dp.message_handler(state=PersonalData.phoneNumber)
async def answer_phone(message: Message, state: FSMContext):
    phone = message.text

    await state.update_data(
        {
            'phoneNumber': phone
        }
    )
    
    data = await state.get_data()
    soha = data.get('qaysi_sohaga')
    fullname = data.get('fullname')
    resume = data.get('resume')
    phone = data.get('phoneNumber')

    msg = (
        "Quyidagi ma'lumotlar qabul qilindi.\n"
        "Tez orada operatorlarimiz bog'lanadi.\n\n\n"
        f"<b>Topshirgan yo'nalshingiz</b>: {soha}\n"
        f"<b>ism familiya sharifi</b>: {fullname}\n"
        f"<b>Rezyumengiz</b>: {resume}\n"
        f"<b>Telefon raqamingiz</b>: {phone}"
    )

    
    # await state.reset_state(with_data=False)
    await message.answer(msg, reply_markup=informatsiya)
    await state.finish()

@dp.callback_query_handler(text="2ortga")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = open("photos/about.jpg",'rb')
    msg = "<b>Menyu:</b>"
    await call.message.answer_photo(photo=photo,caption=msg, reply_markup=menu)