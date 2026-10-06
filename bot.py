import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

logging.basicConfig(level=logging.INFO)
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("⚽ Football", callback_data="sport_football")],
        [InlineKeyboardButton("🏀 Basketball", callback_data="sport_basketball")],
        [InlineKeyboardButton("🎾 Tennis", callback_data="sport_tennis")],
    ]
    await update.message.reply_text(
        "Choose a sport to see latest scores and fixtures:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def scores(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Fetching latest scores...\n\nFootball\nArsenal 2 - 1 Chelsea (FT)\nReal Madrid 3 - 0 Getafe (FT)")

async def fixtures(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Upcoming fixtures:\n\nFootball\nLiverpool vs Man City — Sat 17:30\nBarcelona vs Atletico — Sun 20:00")

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("/start — Main menu\n/scores — Latest scores\n/fixtures — Upcoming matches\n/about — Bot info")

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Sports Score Bot v1.0\nA lightweight bot for checking sports scores and fixtures.")

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    sport = query.data.replace("sport_", "").capitalize()
    await query.edit_message_text(f"Showing {sport} updates...\n\nUse /scores for live results or /fixtures for schedule.")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("scores", scores))
    app.add_handler(CommandHandler("fixtures", fixtures))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.run_polling()

if __name__ == "__main__":
    main()
