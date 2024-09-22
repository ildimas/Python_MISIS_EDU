from aiogram import Router, types, F
from chatgpt_api import ChatGPT_acsess_point
        
main_router = Router()


# @main_router.message()
# async def echo(msg: types.Message) -> None:
#     await msg.answer(msg.text)
    

@main_router.message()
async def gpt_prompt(msg: types.Message) -> None:
    x = ChatGPT_acsess_point(msg.text)
    await msg.answer(await x.wait_for_run_completion())