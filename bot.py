from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# ضع التوكن الخاص بك هنا
TOKEN = "8713896213:AAHlyLBOFiR31gQr7WzpqGHVwktPGwWPwWk"
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # رسالة ترحيبية احترافية
    welcome_text = (
        "🛡️ *Welcome to SafeScan AI Official Bot!*\n\n"
        "I can help you check any URL for phishing, malware, or suspicious patterns.\n\n"
        "👉 *To start scanning, please use our Global Web Interface below:*"
    )
    
    # زر يوجه المستخدم لموقعك على GitHub
    keyboard = [
        [InlineKeyboardButton("🌐 Open SafeScan Web Terminal", url="https://islemzebouchi-afk.github.io/safescan-ai/")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(welcome_text, reply_markup=reply_markup, parse_mode='Markdown')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # إذا أرسل المستخدم أي نص أو رابط، نوجهه للموقع فوراً ليرى الإعلانات
    response_text = (
        "🔍 *Analyzing request...*\n\n"
        "To get the full security report, please complete the scan on our official website:"
    )
    keyboard = [[InlineKeyboardButton("✅ View Full Security Report", url="https://islemzebouchi-afk.github.io/safescan-ai/")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(response_text, reply_markup=reply_markup, parse_mode='Markdown')

if __name__ == '__main__':
    print("Bot is starting...")
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    app.run_polling()