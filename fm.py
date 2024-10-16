import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import subprocess

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Define your radio stations
RADIO_STATION = {
    "Air Bilaspur": "http://air.pc.cdn.bitgravity.com/air/live/pbaudio110/playlist.m3u8",
    "Air Raipur": "http://air.pc.cdn.bitgravity.com/air/live/pbaudio118/playlist.m3u8",
    "Capital FM": "http://media-ice.musicradio.com/CapitalMP3?.mp3&listening-from-radio-garden=1616312105154",
    "English": "https://hls-01-regions.emgsound.ru/11_msk/playlist.m3u8",
    "Mirchi": "http://peridot.streamguys.com:7150/Mirchi",
    "Radio Today": "http://stream.zenolive.com/8wv4d8g4344tv",
    "YouTube": "https://www.youtube.com/live/eu191hR_LEc?si=T-9QYD548jd0Mogp",
    "Zee News": "https://www.youtube.com/live/TPcmrPrygDc?si=hiHBkIidgurQAd1P",
    "Aaj Tak": "https://www.youtube.com/live/Nq2wYlWFucg?si=usY4UYiSBInKA0S1",
}

# Command to start the bot
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Welcome to the Radio Stream Bot! Use /stations to see the available stations.")

# List available radio stations
def stations(update: Update, context: CallbackContext) -> None:
    stations_list = "n".join(RADIO_STATION.keys())
    update.message.reply_text(f"Available stations:n{stations_list}")

# Play a selected radio station
def play(update: Update, context: CallbackContext) -> None:
    if context.args:
        station_name = " ".join(context.args)
        if station_name in RADIO_STATION:
            update.message.reply_text(f"Playing {station_name}...")
            stream_url = RADIO_STATION[station_name]
            # Start the FFmpeg process to stream audio
            subprocess.Popen(['ffmpeg', '-i', stream_url, '-f', 'mp3', 'pipe:1'], stdout=subprocess.PIPE)
        else:
            update.message.reply_text("Station not found. Use /stations to see available stations.")
    else:
        update.message.reply_text("Please specify a station name. Usage: /play <station_name>")

# Main function to run the bot
def main() -> None:
    # Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual bot token
    updater = Updater("7856951971:AAHhnHq_LTdvjC-cBrIuonXeJSzOfLNC7so")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("stations", stations))
    dispatcher.add_handler(CommandHandler("play", play))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()