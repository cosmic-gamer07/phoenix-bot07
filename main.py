import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import os

TOKEN = os.environ.get("BOT_TOKEN")
CHANNEL_USERNAME = "@phoenixverse_07"
APP_LINK = "https://yourapplink.com"

bot = telebot.TeleBot(TOKEN)

def check_join(user_id):
    try:
        member = bot.get_chat_member(CHANNEL_USERNAME, user_id)
        return member.status in ['member', 'administrator', 'creator']
    except:
        return False

@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup()
    join_btn = InlineKeyboardButton("Join Channel", url="https://t.me/phoenixverse_07")
    check_btn = InlineKeyboardButton("Try Again", callback_data="check_join")
    markup.add(join_btn)
    markup.add(check_btn)

    bot.send_message(
        message.chat.id,
        "To use this bot, first join our channel.",
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: call.data == "check_join")
def callback_check(call):
    if check_join(call.from_user.id):
        bot.send_message(call.message.chat.id, f"✅ Access Granted!\nDownload here:\n{APP_LINK}")
    else:
        bot.answer_callback_query(call.id, "❌ You have not joined yet!")

bot.polling()
