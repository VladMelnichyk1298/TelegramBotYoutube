from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустити бота"),
            types.BotCommand("help", "Вивести довідку"),
            types.BotCommand("audio", "Завантажити відео з ютуба та перекласти в аудіо")
        ]
    )
