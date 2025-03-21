# Import کردن کتابخانه‌های موردنیاز
import requests
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# ===================== [ تنظیمات اولیه ] =====================
# توکن ربات تلگرام
TELEGRAM_BOT_TOKEN = "7823007893:AAH-BZKK2lhZ-VZS4KXc-SPSQSktR3pyBDQ"

# API چت جی‌پی‌تی
GPT_API_URL = "https://yw85opafq6.execute-api.us-east-1.amazonaws.com/default/boss_mode_15aug"

# راه‌اندازی لاگ‌گیری برای دیباگ
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

# ===================== [ تابع درخواست به چت جی‌پی‌تی ] =====================
def chat_with_gpt(text):
    payload = {"text": text, "country": "Asia", "user_id": "usery3peypi26p"}
    
    response = requests.post(GPT_API_URL, json=payload)
    
    if response.status_code == 200:
        return response.text  # بازگرداندن مستقیم پاسخ
    else:
        return "مشکلی پیش اومده! لطفاً دوباره تلاش کن."

# ===================== [ هندلر استارت ] =====================
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("سلام! من ربات هوش مصنوعی هستم. سوالت رو بفرست 😊")

# ===================== [ هندلر پیام‌ها ] =====================
async def handle_message(update: Update, context: CallbackContext):
    user_message = update.message.text  # گرفتن پیام کاربر
    response = chat_with_gpt(user_message)  # فرستادن پیام به API و دریافت پاسخ
    await update.message.reply_text(response)  # ارسال پاسخ به کاربر

# ===================== [ راه‌اندازی ربات ] =====================
def main():
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    
    # اضافه کردن هندلرها
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("ربات فعال شد...")
    app.run_polling()

# اجرای ربات
if __name__ == "__main__":
    main()
