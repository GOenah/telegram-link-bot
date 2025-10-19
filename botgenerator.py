from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random

# ================================
# GANTI TOKEN DI SINI
TOKEN = "8275165128:AAEbPQ1fOvhl2dG2qB98KDGR2euXgi1A7CI"
# ================================

# Link dasar yang angka 6258731000-nya akan diganti secara acak
BASE_LINK = (
    "https://ton.holos-market.com/#tgWebAppData=user%3D%257B%2522id%2522%253A6258731000"
    "%252C%2522first_name%2522%253A%2522Sana%2520JI88%25F0%259F%25A6%25B4%2520%25F0%259F%2590"
    "%2588%25E2%2580%258D%25E2%25AC%259B%25F0%259F%2590%25BE%2522%252C%2522last_name%2522%253A"
    "%2522%2522%252C%2522username%2522%253A%2522sanaj210%2522%252C%2522language_code%2522%253A"
    "%2522en%2522%252C%2522allows_write_to_pm%2522%253Atrue%252C%2522photo_url%2522%253A%2522"
    "https%253A%255C%252F%255C%252Ft.me%255C%252Fi%255C%252Fuserpic%255C%252F320%255C%252F"
    "ik404bcQ4n2nRj1Oa4E5yta_C6BS-w5rA1bltM8g0jqTGb6THeXfXHfBVLUs1JsL.svg%2522%257D"
)

# ================================
# Fungsi command /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("User menekan /start")
    await update.message.reply_text(
        "👋 Halo!\nKetik perintah seperti ini untuk membuat link:\n\n"
        "/gen 5 → untuk membuat 5 link acak\n\n"
        "Setiap link nanti otomatis bisa diklik langsung ✅"
    )

# ================================
# Fungsi command /gen
async def generate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("Perintah /gen diterima!")  # muncul di terminal
    try:
        n = int(context.args[0])
    except (IndexError, ValueError):
        await update.message.reply_text("Gunakan format: /gen <jumlah>\nContoh: /gen 5")
        return

    results = []
    for i in range(n):
        random_num = random.randint(6000000000, 6999999999)
        new_link = BASE_LINK.replace("6258731000", str(random_num))
        results.append(f"[🔗 Link {i+1}]({new_link})")

    reply = "Berikut hasil generate link kamu:\n\n" + "\n".join(results)
    await update.message.reply_text(reply, parse_mode="Markdown", disable_web_page_preview=True)

# ================================
# Menjalankan bot
if __name__ == "__main__":
    print("Menjalankan bot...")
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("gen", generate))
    app.run_polling()
