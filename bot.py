from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from zz import spam  # Lấy hàm spam từ zz.py

BOT_TOKEN = "7864938791:AAGk6Lkp4uzHvOFp_4K-kywqqNovkWTw790"  # ← THAY bằng token bot của bạn
AUTHOR_NAME = "KHANHH HUYENN"
...
f"👤 Bot được tạo bởi: {AUTHOR_NAME}\n"

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"👤 Bot được tạo bởi: KHANHH HUYENN\n"
        "📜 Lệnh: /Locket spam [url] [số luồng] [tin nhắn]"
    )

async def locket(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    if len(args) < 4 or args[0].lower() != "spam":
        await update.message.reply_text("❗ Cú pháp đúng: /Locket spam [url] [số luồng] [tin nhắn]")
        return

    url = args[1]
    try:
        threads = int(args[2])
    except ValueError:
        await update.message.reply_text("❗ Số luồng phải là số.")
        return

    message = ' '.join(args[3:])
    await update.message.reply_text(f"🚀 Bắt đầu spam: {url} ({threads} luồng)\n💬 Nội dung: {message}")
    spam(url, threads, message)

async def ag(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Lệnh /ag đã được kích hoạt!")

app = ApplicationBuilder().token(7864938791:AAGk6Lkp4uzHvOFp_4K-kywqqNovkWTw790).build()
app.add_handler(CommandHandler("menu", menu))
app.add_handler(CommandHandler("Locket", locket))
app.add_handler(CommandHandler("ag", ag))

print("🤖 Bot đã sẵn sàng...")
app.run_polling()
