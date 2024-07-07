import asyncio
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

API_KEY = '7023573128:AAHHKfedF-Usve1mMqGtZ6Rqd7SkBYm6GDE'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Send a photo
    photo_url = "https://i.ytimg.com/vi/FJdPymT2MV0/maxresdefault.jpg"
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=photo_url)

    # Send a welcome text message
    welcome_text = "🤖𝗪𝗘𝗟𝗖𝗢𝗠𝗘 𝗧𝗢 𝗦𝗧𝗔𝗞𝗘 𝗙𝗥𝗘𝗘 𝗕𝗢𝗧🤖"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=welcome_text)

    # Send an inline button
    button = InlineKeyboardButton(text="GET STARTED", callback_data='select_bot')
    reply_markup = InlineKeyboardMarkup([[button]])
    await context.bot.send_message(chat_id=update.effective_chat.id, text="⬇️ 𝗦𝗲𝗹𝗲𝗰𝘁 𝘄𝗵𝗶𝗰𝗵 𝗕𝗼𝘁 𝘆𝗼𝘂 𝘄𝗮𝗻𝘁 ⬇️", reply_markup=reply_markup)

async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    # The next text message
    next_text = """𝗜𝗡𝗙𝗢 ⬇

🟩 𝗩𝗜𝗣 𝗕𝗢𝗧 𝟵𝟴.𝟵𝟵% 𝗔𝗖𝗖𝗨𝗥𝗔𝗖𝗬 🎯 𝗔𝗡𝗗 𝗔𝗣𝗜 𝗦𝗨𝗣𝗣𝗢𝗥𝗧 ⚡️

𝗩𝗜𝗣 𝗕𝗢𝗧 - (𝟰𝟵𝟵₹) 𝗟𝗶𝗳𝗲𝘁𝗶𝗺𝗲 𝗔𝗰𝗰𝗲𝘀𝘀
Admin - @stakes_mine_support

🟥𝗙𝗥𝗘𝗘 𝗕𝗢𝗧 𝟳𝟮.𝟳% 𝗔𝗖𝗖𝗨𝗥𝗔𝗖𝗬 🎯 𝗔𝗡𝗗 𝗡𝗢𝗧 𝗔𝗣𝗜 𝗦𝗨𝗣𝗣𝗢𝗥𝗧 🚫

"""

    # Buttons for "FREE BOT" and "PAID BOT"
    free_bot_button = InlineKeyboardButton(text="FREE BOT 🤖", callback_data='free_bot_info')
    paid_bot_button = InlineKeyboardButton(text="VIP BOT 💲", callback_data='vip_bot')
    reply_markup = InlineKeyboardMarkup([[free_bot_button, paid_bot_button]])

    await query.edit_message_text(text=next_text, reply_markup=reply_markup)

async def free_bot_info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    # Text for free bot info
    free_bot_text = """⚠️ 𝗔𝘁𝘁𝗲𝗻𝘁𝗶𝗼𝗻 📣

✳️ 𝗬𝗼𝘂 𝗰𝗮𝗻 𝘂𝘀𝗲 𝘁𝗵𝗲 𝗳𝗿𝗲𝗲 𝘃𝗲𝗿𝘀𝗶𝗼𝗻 🆓

💀 𝗟𝗶𝘁𝘁𝗹𝗲 𝗥𝗶𝘀𝗸𝘆 𝗔𝗹𝘄𝗮𝘆𝘀 𝗣𝗹𝗮𝘆 𝟱% 𝗢𝗙 𝗕𝗮𝗻𝗸𝗿𝗼𝗹𝗹

🎯 𝟳𝟮% 𝗮𝗰𝗰𝘂𝗿𝗮𝗰𝘆 𝗶𝗻 𝗙𝗿𝗲𝗲 𝘃𝗲𝗿𝘀𝗶𝗼𝗻 🤖

🔺 𝗕𝗘𝗧 𝗦𝗠𝗔𝗟𝗟 𝗔𝗠𝗢𝗨𝗡𝗧

𝗖𝗼𝗻𝘁𝗮𝗰𝘁 - @stakes_mine_support

"""

    # Button to select number of mines
    select_mines_button = InlineKeyboardButton(text="SELECT NUMBER OF MINES 💣", callback_data='select_mines')
    reply_markup = InlineKeyboardMarkup([[select_mines_button]])

    await query.edit_message_text(text=free_bot_text, reply_markup=reply_markup)

async def select_mines(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    # Text for selecting the number of mines
    select_text = "💣𝗦𝗲𝗹𝗲𝗰𝘁 𝘁𝗵𝗲 𝗛𝗼𝘄 𝗠𝗮𝗻𝘆 𝗠𝗶𝗻𝗲𝘀⬇️"

    # Creating buttons 1 to 10 with specified labels
    buttons = [
        [InlineKeyboardButton(text="1 [FREE] 72% ACCURACY", callback_data='mines_1')],
        [InlineKeyboardButton(text="2 [FREE] 72% ACCURACY", callback_data='mines_2')],
        [InlineKeyboardButton(text="3 [VIP]", callback_data='vip_bot')],
        [InlineKeyboardButton(text="4 [VIP]", callback_data='vip_bot')],
        [InlineKeyboardButton(text="5 [VIP]", callback_data='vip_bot')],
        [InlineKeyboardButton(text="6 [VIP]", callback_data='vip_bot')],
        [InlineKeyboardButton(text="7 [VIP]", callback_data='vip_bot')],
        [InlineKeyboardButton(text="8 [VIP]", callback_data='vip_bot')],
        [InlineKeyboardButton(text="9 [VIP]", callback_data='vip_bot')],
        [InlineKeyboardButton(text="10 [VIP]", callback_data='vip_bot')]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)

    await query.edit_message_text(text=select_text, reply_markup=reply_markup)

async def mines_1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    # Send image and ask for server seed
    image_url = "https://i.postimg.cc/WbxhZNsS/photo-2024-03-29-14-07-57.jpg"
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=image_url)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="𝗙𝗶𝗻𝗱 𝘆𝗼𝘂𝗿 (𝗔𝗰𝘁𝗶𝘃𝗲 𝗦𝗲𝗿𝘃𝗲𝗿 𝗦𝗲𝗲𝗱) 𝗮𝗻𝗱 𝗽𝗮𝘀𝘁𝗲 𝗶𝘁 𝗵𝗲𝗿𝗲 👇👇")

    # Set the state for waiting for user input
    context.user_data['awaiting_server_seed'] = 'mines_1'

async def mines_2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    # Send image and ask for server seed
    image_url = "https://i.postimg.cc/WbxhZNsS/photo-2024-03-29-14-07-57.jpg"
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=image_url)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="𝗙𝗶𝗻𝗱 𝘆𝗼𝘂𝗿 (𝗔𝗰𝘁𝗶𝘃𝗲 𝗦𝗲𝗿𝘃𝗲𝗿 𝗦𝗲𝗲𝗱) 𝗮𝗻𝗱 𝗽𝗮𝘀𝘁𝗲 𝗶𝘁 𝗵𝗲𝗿𝗲 👇👇")

    # Set the state for waiting for user input
    context.user_data['awaiting_server_seed'] = 'mines_2'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Check if we are awaiting server seed input
    if 'awaiting_server_seed' in context.user_data:
        if context.user_data['awaiting_server_seed'] == 'mines_1' or context.user_data['awaiting_server_seed'] == 'mines_2':
            user_input = update.message.text
            if len(user_input) == 64:
                await context.bot.send_message(chat_id=update.effective_chat.id, text="LOADING...")
                await asyncio.sleep(3)

                # Button to open telegra.ph and web app mini feature
                telegra_button = InlineKeyboardButton(text="💎CLICK HERE💎", web_app=WebAppInfo(url="https://2minesnet.netlify.app/"))
                reply_markup = InlineKeyboardMarkup([[telegra_button]])

                await context.bot.send_message(chat_id=update.effective_chat.id, text="⬇️𝗥𝗲𝘀𝘂𝗹𝘁 𝗶𝘀 𝗿𝗲𝗮𝗱𝘆⬇️", reply_markup=reply_markup)
            else:
                await context.bot.send_message(chat_id=update.effective_chat.id, text="Invalid server seed /start")
            return
         # Handle other text messages here if needed
    await context.bot.send_message(chat_id=update.effective_chat.id, text="""❌ Unknown Command!

You have send a Message directly into the Bot's chat or
Menu structure has been modified by Admin.

ℹ️ Do not send Messages directly to the Bot or
reload the Menu by pressing /start""")

async def vip_bot(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    # Display VIP bot information
    vip_text = """𝗩𝗜𝗣 𝗕𝗢𝗧 𝗗𝗘𝗧𝗔𝗜𝗟𝗦 💎

 🎯𝗔𝗰𝗰𝘂𝗿𝗮𝗰𝘆: 𝟵𝟴.𝟵𝟵%

 ⚡️ 𝟮𝘅+ 𝗖𝗮𝘀𝗵𝗼𝘂𝘁

 ♾️ 𝗨𝗻𝗹𝗶𝗺𝗶𝘁𝗲𝗱 𝗨𝘀𝗲 

✅ 𝗧𝗼 𝗯𝘂𝘆, 𝗽𝗹𝗲𝗮𝘀𝗲 𝗰𝗹𝗶𝗰𝗸 𝘁𝗵𝗲 𝗯𝘂𝘆 𝗻𝗼𝘄 𝗯𝘂𝘁𝘁𝗼𝗻.

🎟️ 𝗕𝗲𝗰𝗼𝗺𝗲 𝗮 𝗩𝗜𝗣 𝗻𝗼𝘄!"""

    # Button to buy VIP bot
    buy_now_button = InlineKeyboardButton(text="BUY NOW 💳", callback_data='buy_now')
    reply_markup = InlineKeyboardMarkup([[buy_now_button]])

    await query.edit_message_text(text=vip_text, reply_markup=reply_markup)

async def buy_now(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
     
    photo_url = "https://i.postimg.cc/pX0SxJw5/polotno.png"
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=photo_url)

    # Send a welcome text message
    welcome_text = """ 𝗩𝗜𝗣 𝗕𝗢𝗧 - 𝟰𝟵𝟵 𝗥𝘂𝗽𝗲𝗲𝘀

𝗦𝗖𝗔𝗡 𝗧𝗛𝗜𝗦  

 stakemines@ybl 
☝️☝️𝗖𝗢𝗣𝗬 𝗨𝗣𝗜 𝗜𝗗☝️☝️ 

𝗣𝗔𝗬 & 𝗦𝗘𝗡𝗗 𝗦𝗖𝗥𝗘𝗘𝗡𝗦𝗛𝗢𝗧 
@stakes_mine_support

𝗪𝗶𝘁𝗵𝗶𝗻 𝟭𝟱 𝗠𝗶𝗻𝘀 𝗬𝗼𝘂 𝗪𝗶𝗹𝗹 𝗚𝗲𝘁 𝗣𝗮𝗶𝗱 𝗕𝗼𝘁  🤖"""
    await context.bot.send_message(chat_id=update.effective_chat.id, text=welcome_text)
     
    confirm_payment_button = InlineKeyboardButton(text="CONFIRM PAYMENT ✅", callback_data='payment_confirm')
    reply_markup = InlineKeyboardMarkup([[confirm_payment_button]])
    

async def payment_confirm(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    # Confirmation message
    confirmation_text = "Thank you for your payment! Please send the screenshot of your payment to @stakes_mine_support for verification."

    await query.edit_message_text(text=confirmation_text)

if __name__ == '__main__':
    app = ApplicationBuilder().token(API_KEY).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CallbackQueryHandler(button_click, pattern='select_bot'))
    app.add_handler(CallbackQueryHandler(free_bot_info, pattern='free_bot_info'))
    app.add_handler(CallbackQueryHandler(select_mines, pattern='select_mines'))
    app.add_handler(CallbackQueryHandler(mines_1, pattern='mines_1'))
    app.add_handler(CallbackQueryHandler(mines_2, pattern='mines_2'))
    app.add_handler(CallbackQueryHandler(vip_bot, pattern='vip_bot'))
    app.add_handler(CallbackQueryHandler(buy_now, pattern='buy_now'))
    app.add_handler(CallbackQueryHandler(payment_confirm, pattern='payment_confirm'))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()
